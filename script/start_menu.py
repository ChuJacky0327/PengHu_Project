import requests
'''
到start_menu.py這裡執行要更改richmenu的ID和token，這樣就會跳出圖文選單了
'''
headers = {"Authorization":"Bearer zzBhAZ4MBDEhL2RWVLLCq8GJhQI3PCiV9IU4DZh4nQw3PCXBKHjw6DMkMFx2ZEyADX42DEwByiyq96zeUUn6gyA7GPrwuGTS5vV3IzqI89/6BTEN46OW0ZiDnq7n/eQMg/7DCAI2IXTpydRXac3ZPgdB04t89/1O/w1cDnyilFU=","Content-Type":"application/json"}

req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/richmenu-f10a1523d22f9aea0c6ec17d3aa5d0e9', 
                       headers=headers)

print(req.text)