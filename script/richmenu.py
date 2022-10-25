import requests
import json
'''
先在richmenu.py設定要傳入的token，還有要設定的圖文選單，並找到richmenu的ID
ps.每次richmenu的ID都會更改
再到menu_backgroune.py改背景
'''
def menu():
    token="zzBhAZ4MBDEhL2RWVLLCq8GJhQI3PCiV9IU4DZh4nQw3PCXBKHjw6DMkMFx2ZEyADX42DEwByiyq96zeUUn6gyA7GPrwuGTS5vV3IzqI89/6BTEN46OW0ZiDnq7n/eQMg/7DCAI2IXTpydRXac3ZPgdB04t89/1O/w1cDnyilFU="
    headers = {"Authorization":"Bearer "+token,"Content-Type":"application/json"}
    
    body = {
        "size": {"width": 2500, "height": 843},#目前寬度僅能設置 2500 ，高度有 843 或 1686 兩種選擇
        "selected": "false",
        "name": "選擇您需要的功能",
        "chatBarText": "點我收合選單",
        "areas":[
            {
              "bounds": {"x": 0, "y": 0, "width": 833, "height": 843},
              "action": {"type": "message", "text": "行程規劃"},
              "label":"行程規劃"
            },
            {
              "bounds": {"x": 833, "y":0 , "width": 833, "height": 843},
              "action": {"type": "message", "text": "景點推薦"},
              "label":"景點推薦"
            },
            {
              "bounds": {"x": 1666, "y":0 , "width": 833, "height": 843},
              "action": {"type": "message", "text": "景點人潮"},
              "label":"景點人潮"
            }
        ]
      }
    
    req = requests.request('POST', "https://api.line.me/v2/bot/richmenu",headers=headers,data=json.dumps(body).encode('utf-8'))
    print(req.text)
    
menu()

