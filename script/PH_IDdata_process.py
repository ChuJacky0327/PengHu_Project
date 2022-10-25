#第二版機器學習(先判斷使用者是否有出現在beacon資料集中，使用者有出現過的地方就刪掉檔案再做機器學習，沒有出現過直接坐機器學習)
import pandas as pd
import pymysql
def UUID_Process(user_id):
    beacon = pd.read_csv('penghu_orignal.csv',encoding='utf-8-sig')
    beacon_no = beacon["no"]
    beacon_id = beacon["UserID/MemID"]
    beacon_local = beacon["設置點"]
    id_user = user_id#改成line bot使用者讀到的user id 
    #U9572c40391eaf8b27a9d4
    #id_user = ('U957b27a9d4')
    same_userid = (beacon_id == id_user)#判斷是否為相同ID
    #print(same_userid)
    number_same_userid = beacon_no[same_userid]#相同ID是哪些
    #print(type(number_same_userid))
    id_check = number_same_userid.empty
    #print((id_check))
    
    if (id_check == False):
        local_id = beacon_local[number_same_userid]#ID的設置點(地點)有哪些
    
        beacon_Different = {}
        name = local_id.value_counts()#去判斷有幾個種類的設置點
    
        local_id.reset_index(inplace=True, drop=True)#把找到ID的index排序重排
        #print(local_id)
    
        #先做第一個設置點的刪除
        local_1 = local_id[0]
        #print("local_1",local_1)
        local_same = (beacon_local == local_1)#找尋所有beacon符合使用者第一個的設置點
        beacon_Different = beacon.drop(beacon_no[local_same], axis = 0)#直接抓相同設置點對應的number刪掉
        #beacon_Different.to_csv("penghu_orignal2.csv",encoding='utf-8-sig')
    
        #第二個以後的設置點用迴圈判斷
        for i in range (1,name.shape[0]):
            local_1 = local_id[i]
            local_same = (beacon_local == local_1)
            beacon_Different = beacon_Different.drop(beacon_no[local_same], axis = 0)#後面迴圈直接覆蓋
            #id_user = str(id_user)
            #print(beacon_Different)
            #print("------------------")
            beacon_Different.to_csv("penghu_orignal2.csv",encoding='utf-8-sig',index = False) 
    
            #beacon = pd.read_csv('penghu_orignal2.csv',encoding='utf-8-sig')
        #print(beacon_Different)
    else:
        beacon.to_csv("penghu_orignal2.csv",encoding='utf-8-sig',index = False) 
    print('processOK')
    
    
def UUID_Plan(plan_UUID, plan_data):
    beacon = plan_data
    beacon_no = beacon["no"]
    beacon_id = beacon["UserID/MemID"]
    beacon_local = beacon["設置點"]
    beacon_latitude = beacon["緯度"]
    beacon_longitude = beacon["經度"]
    beacon_time = beacon["Time"]
    #print(beacon_time[0])
    print(beacon_no.shape[0])
    plan_no = {}
    plan_time = {}#dict型態
    plan_latitude = {}#dict型態
    plan_longitude = {}#dict型態
    plan_local = {}#dict型態
    #print(type(beacon_time)) #是pd的型態所以無法直接存矩陣，要存在{}
    for i in range(0,beacon_no.shape[0]):
        if beacon_id[i] == plan_UUID : 
            plan_no[i] = i
            plan_time[i] = beacon_time[i]
            plan_latitude[i] = beacon_latitude[i]
            plan_longitude[i] = beacon_longitude[i]
            plan_local[i] = beacon_local[i]
    pd_no = pd.DataFrame([plan_no])
    pd_time = pd.DataFrame([plan_time])#轉回pd型態
    pd_latitude = pd.DataFrame([plan_latitude])#轉回pd型態
    pd_longitude = pd.DataFrame([plan_longitude])#轉回pd型態
    pd_local = pd.DataFrame([plan_local])#轉回pd型態
    result = pd.concat([pd_no,pd_time,pd_latitude,pd_longitude,pd_local], axis=0)#pd合併
    result = result.transpose()#轉置
    #print(result)
    result.to_csv("realtime_plan.csv",encoding='utf-8-sig',index = False) 
    print('realtime_plan.csv OK')    


def plan_toSQL():
    with open("realtime_plan.csv","r",encoding="utf-8") as reader:
        data= reader.readlines()
        #print (data.head(1)) #列印前5行
        data_list = []
        for i in data:
            tp=tuple(i.strip().split(","))#strip()移除空格和換行
            data_list.append(tp)
        insert_list=data_list[1:]#因為設1,所以沒有存標頭,標頭資料庫建表的時候就會設好了
        #print(insert_list[0])
        #print(np.array(data).shape)
        #print(insert_list[0])
    with pymysql.connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         password='0327',
                         database='penghu',#資料庫(create database)的名稱
                         charset='utf8') as conn:
        sql = """DELETE FROM realtimeplan"""
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        
        sql = "INSERT INTO realtimeplan values(%s,%s,%s,%s,%s)" #(penghudata為penghu資料庫的資料表)
        cur.executemany(sql,insert_list)
        conn.commit()
    cur.close()
    print("csv already save in MySQL")


















