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

line_bot_api = LineBotApi('')

with open("1111.jpg", 'rb') as f:
    line_bot_api.set_rich_menu_image("richmenu-f10a1523d22f9aea0c6ec17d3aa5d0e9", "image/jpeg", f)
#傳入的圖片無法再傳入
