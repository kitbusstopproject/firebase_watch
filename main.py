import firebase_admin
from firebase_admin import db
import time
import requests
import os
import threading
import json

#firebaseの認証キーはGOOGLE_APPLICATION_CREDENTIALSに環境変数として設定する

#slack HTTP POSTのURL
#OSの環境変数にしたい
url = "https://dokoka_tekitouna_slack_url.com"

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
            print(f'{path}: {data} 初回')
            prev_data[path] = data
            requests.post(url, data = json.dumps({
                'text': f'{path}: {data} 初回'
            }))

        #正常更新の場合はデータを格納して終了
        elif data != prev_data[path]:
            print(f'{path}: {data} 更新あり')
            prev_data[path] = data
            requests.post(url, data = json.dumps({
                'text': f'{path}: {data} 更新あり'
            }))

        #更新がない場合slackに通知
        elif data == prev_data[path]:
            print(f'{path}: {data} 更新なし')
            requests.post(url, data = json.dumps({
                'text': f'{path}: {data} 更新なし'
            }))

#def main():



if __name__ == '__main__':
  
  threads = []

  while True:
    print("while")
    for path in paths:
      print("for")  
      t = threading.Thread(target=check_data, args=(path,))
      threads.append(t)
      t.start()
    for t in threads:
        t.join()
        time.sleep(60)
