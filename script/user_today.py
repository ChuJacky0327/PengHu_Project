#爬蟲使用者當下天氣並比對
import requests
from bs4 import BeautifulSoup
from opencc import OpenCC
import random
import pandas as pd
import re
import time
import csv


def today_weather():
    #當天天氣爬蟲
    response = requests.get("https://www.tianqi24.com/penghu.html")
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("section")
    a = result.select("article")
    b = a[1].select("section")
    c = b[0].select("li")
    c = c[1].select("div")
    characters = "/0 <div>/bspan"
    date = str(c[2])
    #print((date))
    date = date.replace('\n','')
    date = date.replace(" ", "")
    date = ''.join( x for x in date if x not in characters)
    cc = OpenCC('s2t')
    weather = cc.convert(date[0:5])
    weather = weather.replace("\s", "")
    weather_orignal = weather
    #print(weather_orignal)
    weather_orignal = re.sub(r"\s+$", "", weather_orignal)
    #print((weather_orignal))
    
    
    #比對天氣是否有出在資料庫中
    beacon = pd.read_csv('penghu_orignal.csv',encoding='utf-8-sig')
    beacon_wh = beacon["weather"]
    beacon_wh_num = beacon_wh.unique()#哪些種類天氣
    #beacon_wh_num = beacon_wh.value_counts()#重複數量多少
    #print(beacon_wh_num)
    
    for i in range (0,25):
        same_userid = (weather_orignal == beacon_wh_num)
        
        if same_userid[i] == True:#判斷使用者當下天氣比對所有天氣種類，有一樣直接break
            #print(same_userid[i])
            #print(date)
            weather = weather_orignal 
            break
        else:#沒有一樣隨機給值
            random_weather = random.randint(0,24)
            weather = beacon_wh_num[random_weather]
            
    print(weather)#最終天氣出來結果
    return weather

def today_temperature():
    response = requests.get("https://weather.yam.com/%E9%A6%AC%E5%85%AC%E5%B8%82/%E6%BE%8E%E6%B9%96%E7%B8%A3")
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("body")
    
    a = result.select("div")
    #a = a.select("div")
    #a = a.select("div")
    #print(a[12])
    temp = str(a[12])
    temp = re.sub("℃",'', temp)
    temp = re.sub("</div>",'', temp)
    temp = re.sub("<div class=>",'', temp)
    temp = re.sub("tempB",'', temp)
    temp = re.sub('"','', temp)
    temp = re.sub('>','', temp)
    characters = "\n\r <div class="
    temp = ''.join( x for x in temp if x not in characters)
    
    print(temp)
    return temp
 
  
    
def today_tidal():
    response = requests.get("https://www.migrator.com.tw/tw/events/%E6%9C%AA%E4%BE%86%E4%B8%80%E5%80%8B%E6%9C%88%E6%BD%AE%E6%B1%90%E9%A0%90%E5%A0%B1.html")
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find("table")
    a = result.select("td")
    #a = a.select("tr")
    #print(a)
    #抓取第一個潮汐狀態
    characters = "</td"
    high1 = str(a[2])
    high1 = high1.split(">")
    high1 = high1[1]
    high1 = ''.join( x for x in high1 if x not in characters)
    
    low1 = str(a[3])
    low1 = low1.split(">")
    low1 = low1[1]
    low1 = ''.join( x for x in low1 if x not in characters)
    
    high =high1.split(":") 
    low =low1.split(":") 
    
    high_min = int(high[0])*60 + int(high[1]) 
    low_min = int(low[0])*60 + int(low[1])  
    range_hour = 60
    
    localtime = time.localtime()
    local_time = int(localtime[3])*60+int(localtime[4])
    #增加第二個的潮汐狀態
    if high_min > 670 :
        high_min2 = high_min -770
    else:
        high_min2 = high_min +770
    if low_min > 670:
        low_min2 = low_min-770
    else:
        low_min2 = low_min+770
    #判斷潮汐
    if (high_min-range_hour < local_time and local_time < high_min+range_hour) or (high_min2-range_hour < local_time and local_time < high_min2+range_hour):
        tidal = 2
    elif (low_min-range_hour < local_time and local_time < low_min+range_hour) or (low_min2-range_hour < local_time and local_time < low_min2+range_hour):
        tidal = 0
    else:
        tidal = 1
    #tidal就是使用者當下的潮汐狀態
    print(tidal)
    return tidal



    