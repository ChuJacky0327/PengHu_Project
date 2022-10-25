from flask import Flask, request, abort

from linebot import ( LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import*
from linebot.exceptions import LineBotApiError
import multiprocessing as mp
from flask import Flask, request, abort

from linebot import ( LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import*
import numpy as np
import multiprocessing as mp
from pydub import AudioSegment
import tempfile
from random import randrange
#import pymssql
import pandas as pd
import PH_IDdata_process
import PH_ML
import user_today
import PH_Attractions

import time

app = Flask(__name__)

line_bot_api = LineBotApi('zzBhAZ4MBDEhL2RWVLLCq8GJhQI3PCiV9IU4DZh4nQw3PCXBKHjw6DMkMFx2ZEyADX42DEwByiyq96zeUUn6gyA7GPrwuGTS5vV3IzqI89/6BTEN46OW0ZiDnq7n/eQMg/7DCAI2IXTpydRXac3ZPgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('cee011ae1ae2e0004fcc13a0584c16d5')
PHP_ngrok = "https://a662-36-231-209-188.ngrok.io"

def travel_reply(Title,label1,text1,data1,label2,text2,data2,label3,text3,data3,label4,text4,data4):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            #最上層
            hero=ImageComponent(
                    url='https://i.imgur.com/W7kiWQT.png',
                    size='full',
                    aspect_ratio='20:13',
                    aspect_mode='cover',
            ),
            #中間層
            body=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text="請選擇您的行程規劃天數",size='xl',color='#000000')
                ],
            ),
            #最下層
            footer=BoxComponent(
                layout='vertical',
                spacing='xs',
                contents=[
                    # websiteAction
                    ButtonComponent(
                        style='secondary',
                        color='#FFEE99',
                        height='sm',
                        action=PostbackAction(label=label1,text=text1,data=data1)
                    ),
                    SeparatorComponent(color='#000000'),
                    # websiteAction
                    ButtonComponent(
                        style='secondary',
                        color='#FFEE99',
                        height='sm',
                        action=PostbackAction(label=label2,text=text2,data=data2)#(一定要有label和data)data設定為傳到handle_postback的值，text為使用者這邊跳出的文字
                    ),
                    SeparatorComponent(color='#000000'),
                    # websiteAction
                    ButtonComponent(
                        style='secondary',
                        color='#FFEE99',
                        height='sm',
                        action=PostbackAction(label=label3,text=text3,data=data3)#(一定要有label和data)data設定為傳到handle_postback的值，text為使用者這邊跳出的文字
                    ),
                    SeparatorComponent(color='#000000'),
                    # websiteAction
                    ButtonComponent(
                        style='secondary',
                        color='#FFEE99',
                        height='sm',
                        action=PostbackAction(label=label4,text=text4,data=data4)#(一定要有label和data)data設定為傳到handle_postback的值，text為使用者這邊跳出的文字
                    )
                ]
            ),
        )
        message=FlexSendMessage(alt_text=Title,contents=bubble)
        return message
    except:
         line_bot_api.reply_message(event.reply_token,TextSendMessage("發生錯誤"))

         
         
@handler.add(PostbackEvent)
def  handle_postback(event):
    postback=event.postback.data
    #讀取製作好的兩天一夜、三天兩夜、四天三夜、五天四夜 HTML程式 (年齡性別人數可以再做選單，但會不會納入HTML程式待定)
    #再補年齡性別人數的選單
    if postback=="兩天一夜":
        #line_bot_api.reply_message(event.reply_token,[TextSendMessage("以下是為您推薦的景點規劃"),ImageSendMessage(original_content_url="https://i.imgur.com/d36P5tN.jpg",preview_image_url="https://i.imgur.com/d36P5tN.jpg")])
        plan_data = pd.read_csv('plan_2day.csv',encoding='utf-8-sig')
        gender = randrange(0,2)
        age = randrange(15,75)
        plan_UUID = PH_ML.XGboost_plan(plan_data,gender,age)
        PH_IDdata_process.UUID_Plan(plan_UUID, plan_data)
        PH_IDdata_process.plan_toSQL()
        line_bot_api.reply_message(event.reply_token, [TextSendMessage("以使用機器學習依據相關性，找尋過往數據最適合您的兩天一夜行程"),TextSendMessage(str(PHP_ngrok)+"/PengHu_plan.php")])        
    
    elif postback=="三天兩夜":
        #line_bot_api.reply_message(event.reply_token,[TextSendMessage("以下是為您推薦的景點規劃"),ImageSendMessage(original_content_url="https://i.imgur.com/GInaTBy.jpg",preview_image_url="https://i.imgur.com/GInaTBy.jpg")])
        plan_data = pd.read_csv('plan_3day.csv',encoding='utf-8-sig')
        gender = randrange(0,2)
        age = randrange(15,75)
        plan_UUID = PH_ML.XGboost_plan(plan_data,gender,age)
        PH_IDdata_process.UUID_Plan(plan_UUID, plan_data)
        PH_IDdata_process.plan_toSQL()
        line_bot_api.reply_message(event.reply_token, [TextSendMessage("以使用機器學習依據相關性，找尋過往數據最適合您的三天兩夜行程"),TextSendMessage(str(PHP_ngrok)+"/PengHu_plan.php")])
    
    elif postback=="四天三夜":
        #line_bot_api.reply_message(event.reply_token,[TextSendMessage("以下是為您推薦的景點規劃"),ImageSendMessage(original_content_url="https://i.imgur.com/dUNl2HI.jpg",preview_image_url="https://i.imgur.com/dUNl2HI.jpg")])
        plan_data = pd.read_csv('plan_4day.csv',encoding='utf-8-sig')
        gender = randrange(0,2)
        age = randrange(15,75)
        plan_UUID = PH_ML.XGboost_plan(plan_data,gender,age)
        PH_IDdata_process.UUID_Plan(plan_UUID, plan_data)
        PH_IDdata_process.plan_toSQL()
        line_bot_api.reply_message(event.reply_token, [TextSendMessage("以使用機器學習依據相關性，找尋過往數據最適合您的四天三夜行程"),TextSendMessage(str(PHP_ngrok)+"/PengHu_plan.php")])
    
    elif postback=="五天四夜":
        #line_bot_api.reply_message(event.reply_token,[TextSendMessage("以下是為您推薦的景點規劃"),ImageSendMessage(original_content_url="https://i.imgur.com/svqGsoW.jpg",preview_image_url="https://i.imgur.com/svqGsoW.jpg")])
        plan_data = pd.read_csv('plan_5day.csv',encoding='utf-8-sig')
        gender = randrange(0,2)
        age = randrange(15,75)
        plan_UUID = PH_ML.XGboost_plan(plan_data,gender,age)
        PH_IDdata_process.UUID_Plan(plan_UUID, plan_data)
        PH_IDdata_process.plan_toSQL()
        line_bot_api.reply_message(event.reply_token, [TextSendMessage("以使用機器學習依據相關性，找尋過往數據最適合您的五天四夜行程"),TextSendMessage(str(PHP_ngrok)+"/PengHu_plan.php")])




# 監聽所有來自 /callback 的 Post Request
@app.route("/", methods=['POST'])
def callback():
     #get X-Line-Signature header value
     signature = request.headers['X-Line-Signature']
     #get request body as text
     body = request.get_data(as_text=True)
     app.logger.info("Request body: " + body)
     #handle webhook body
     try:
         handler.handle(body, signature)
     except InvalidSignatureError:
         abort(400)
     return 'OK'


# 處理訊息
@handler.add(MessageEvent)
def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(event.reply_token, message)
    #mes=event.message.text
    
    mgtype=event.message.type
    if mgtype=='text':
        text=event.message.text
        reply_message(event)    
    elif mgtype=='audio':
        r = sr.Recognizer()
        message_content = line_bot_api.get_message_content(event.message.id)
        ext = 'mp3'
        try:
            with tempfile.NamedTemporaryFile(prefix=ext + '-', delete=False) as tf:
                for chunk in message_content.iter_content():
                    tf.write(chunk)
                tempfile_path = tf.name
            path = tempfile_path 
            AudioSegment.converter = 'D:/中央通訊碩士/合盟澎湖/Beacon/ffmpeg/bin/ffmpeg.exe'
            sound = AudioSegment.from_file_using_temporary_files(path)
            path = os.path.splitext(path)[0]+'.wav'
            sound.export(path, format="wav")
            with sr.AudioFile(path) as source:
                audio = r.record(source)
        except Exception as e:
            line_bot_api.reply_message(event.reply_token,TextSendMessage('語音無法辨識'))
        os.remove(path)
        text = r.recognize_google(audio,language='zh-TW')
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='你的訊息是=\n'+text))
        print(text)
        reply_message(event)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='語音無法辨識,請再說一次'))
    else:
        
        temp=TextSendMessage('目前不支援此種輸入方式')
        line_bot_api.reply_message(event.reply_token,temp)   
    
    
def reply_message(event):
    mes=event.message.text
    user_id = event.source.user_id
    print('user_id :',user_id)
    profile = line_bot_api.get_profile(user_id)
    #print('使用者名稱 :',profile)
    if mes=="你好":
        line_bot_api.reply_message(event.reply_token,[TextSendMessage("您好!"+ str(profile.display_name)+"，歡迎使用NCU_PengHu機器人"),
                                                      ImageSendMessage(original_content_url=str(profile.picture_url)+".jpg",preview_image_url=str(profile.picture_url)+".jpg"),
                                                      TextSendMessage(str(profile.status_message))
                                                      ])
    elif mes=="行程規劃":#讀取製作好的兩天一夜、三天兩夜、四天三夜、五天四夜 HTML程式 (年齡性別人數可以再做選單，但會不會納入HTML程式待定)
        line_bot_api.reply_message(event.reply_token,[TextSendMessage("請選擇您的行程規劃天數，將以大數據推薦行程"),travel_reply("行程規劃","兩天一夜","兩天一夜","兩天一夜","三天兩夜","三天兩夜","三天兩夜","四天三夜","四天三夜","四天三夜","五天四夜","五天四夜","五天四夜")])
    elif mes=="景點推薦":#依照統計合盟的資料，去看有哪些推薦的景點，用linebot去推送景點名稱，爬蟲爬相關資訊、圖片
        
        PH_IDdata_process.UUID_Process(user_id)
        weather = user_today.today_weather()
        tidal = user_today.today_tidal()
        temperature = 20
        #temperature = user_today.today_temperature()
        gender = randrange(0,2)
        age = randrange(15,75)
        '''
        test = np.array([gender,age])
        print(test)
        recommend = PH_ML.XGboost_push(test)
        '''
        #str1 = '風雨'
        arr = np.array([weather])
        #recommend = PH_ML.RandomForest_push(arr,gender,age)
        recommend = PH_ML.XGboost_newpush(arr,gender,age)
        #recommend = PH_ML.XGboost_newpushadd(arr,gender,age,tidal,temperature)
        recommend_website,recommend_imgur,recommend_map = PH_Attractions.Attractions_recommend(recommend)
        print(recommend_website)
        line_bot_api.reply_message(event.reply_token,[TextSendMessage("感謝等待\n系統以AI大數據機器學習的方式推薦以下適合您的地點"),
                                                      TextSendMessage(str(recommend)),
                                                      ImageSendMessage(original_content_url=str(recommend_imgur)+".jpg",preview_image_url=str(recommend_imgur)+".jpg"),
                                                      TextSendMessage(recommend_website),
                                                      TextSendMessage(recommend_map)
                                                      ])
        #time.sleep(3)
        #print('OK')
    elif mes=="景點人潮":#讀取合盟資料建置HTML網站，依照輸入幾點(時間)，去統計看那個時間的人潮量 #寫到SQL資料庫或許可以解決權限問題
        #line_bot_api.reply_message(event.reply_token, [TextSendMessage("請點選以下網址並輸入時間，將由大數據為您分析這時間的人潮"),TextSendMessage(str(PHP_ngrok)+"/PengHu_time_SQL.php")])
        line_bot_api.reply_message(event.reply_token, [TextSendMessage("請點選以下網址，將由大數據為您分析這時間的人潮"),TextSendMessage(str(PHP_ngrok)+"/PengHu_crowd.php")])
    #else:
    #    line_bot_api.reply_message(event.reply_token,TextSendMessage("您好!親愛的用戶，請輸入正確的關鍵字") )



         
def connect_port():
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
    
def main():
    p1=mp.Process(target=connect_port(),args=())
    p1.start()

import os
if __name__ == '__main__':
    main()
    #port = int(os.environ.get('PORT', 8000))
    #app.run(host='0.0.0.0', port=port)
