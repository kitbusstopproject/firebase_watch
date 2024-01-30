import firebase_admin
from firebase_admin import db
import time
import requests
import os
import threading

#slack HTTP POSTのURL
#OSの環境変数にしたい
url = "URL"

# 監視するパスのリスト 
paths = [
  '/BusLocation/route_c/lat',
  '/BusLocation/route_n/lat',
  '/BusLocation/route_no/lat', 
  '/BusLocation/route_s/lat',
  '/BusLocation/route' 
]

# Firebaseに接続
firebase_admin.initialize_app(options={
  'databaseURL': 'https://buslocationsystem-69.firebaseio.com'
})

# 各パスのprev_dataを格納する辞書
prev_data = {path: None for path in paths}

# Firebaseからデータを取得し、前回のデータと比較
def check_data(path):
    global prev_data
    while True:
        data = db.reference(path).get()

        #初回の場合はデータを格納して終了
        if data is None:
            print(f'{path}: {data}')
            prev_data[path] = data

        #正常更新の場合はデータを格納して終了
        elif data != prev_data[path]:
            print(f'{path}: {data}')
            prev_data[path] = data

        #更新がない場合slackに通知
        elif data == prev_data[path]:
            print(f'{path}: {data} 更新なし')
            requests.post(url, data = json.dumps({
                'text': f'{path}: {data}'
            }))

def main():
    # スレッドを作成し、各パスを監視
    threads = []
    while True:
        for path in paths:
            t = threading.Thread(target=check_data, args=(path,))
            t.start()
            threads.append(t)

        # 各スレッドの終了を待つ
        for t in threads:
            t.join()
        
        time.sleep(100)
