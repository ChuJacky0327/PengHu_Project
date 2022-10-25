import pandas as pd
import pymysql
import time, datetime
import numpy as np

#上傳景點人潮的csv到sql
with open("Beacon20220907-crowd.csv","r",encoding="utf-8") as reader:
    data= reader.readlines()
    #print (data.head(1)) #列印前5行
    data_list = []
    for i in data:
        tp=tuple(i.strip().split(","))#strip()移除空格和換行
        data_list.append(tp)
    insert_list=data_list[1:]#因為設1,所以沒有存標頭,標頭資料庫建表的時候就會設好了
    #print(insert_list[0])
    #print(np.array(data).shape)
    print(data[1])


with pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         password='0327',
                         database='penghu',#資料庫(create database)的名稱
                         charset='utf8') as conn:
        sql = "INSERT INTO crowd values(%s,%s,%s,%s,%s,%s)" #(penghudata為penghu資料庫的資料表)
        cur=conn.cursor()
        cur.executemany(sql,insert_list)
        conn.commit()
        cur.close()
        # 连接关闭
        #conn.close()
        print("csv already save in MySQL")
