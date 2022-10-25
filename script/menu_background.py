from linebot import (
    LineBotApi, WebhookHandler
)
'''
到menu_background.py這裡改圖文選單的背景
size要和richmenu設定相同
輸入richmenu的ID和token
傳入的圖片無法再傳入
再到start_menu.py去執行
'''

line_bot_api = LineBotApi('zzBhAZ4MBDEhL2RWVLLCq8GJhQI3PCiV9IU4DZh4nQw3PCXBKHjw6DMkMFx2ZEyADX42DEwByiyq96zeUUn6gyA7GPrwuGTS5vV3IzqI89/6BTEN46OW0ZiDnq7n/eQMg/7DCAI2IXTpydRXac3ZPgdB04t89/1O/w1cDnyilFU=')

with open("1111.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-f10a1523d22f9aea0c6ec17d3aa5d0e9", "image/jpeg", f)
#傳入的圖片無法再傳入