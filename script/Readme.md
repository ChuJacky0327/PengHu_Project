# Line Bot and Python file  
### 備註 :
> 1. 請先自己於 Line Develop 創好自己的 Bot，將 Bot 改成自己的。
> 2. 這邊程式都已經串接好，不在一一講解每隻程式，只講 Demo 如何運作。  
***
## 將 CSV 檔寫入 MySQL :
```shell
$ python3 CSVtoMYSQL.py
```
***
## 執行 Line Bot :
**
1. 記得要先執行 Bot 然後開啟 ngrok 在到 Line Develop 驗證。
2. 記得自行更換程式裡 PHP ngrok 的網址。
**
```shell
$ python3 NCU_PengHuBot.py
```
***
## 更換圖文選單 :
自行更改圖片與 Bot 的 token，**程式內有註解教學**。
```shell
$ python3 richmenu.py
$ python3 menu_background.py
$ python3 start_menu.py 
```
