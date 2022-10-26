import requests
'''
到start_menu.py這裡執行要更改richmenu的ID和token，這樣就會跳出圖文選單了
'''
headers = {"Authorization":"Bearer ","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-f10a1523d22f9aea0c6ec17d3aa5d0e9', 
                       headers=headers)

print(req.text)
