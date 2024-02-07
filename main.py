import firebase_admin
from firebase_admin import db
from firebase_admin import credentials
import time
import requests
import os
import threading
import json

#firebaseの認証キーはGOOGLE_APPLICATION_CREDENTIALSに環境変数として設定する

#slack HTTP POSTのURL
#OSの環境変数にしたい
url = "https://hooks.slack.com/services/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"

# 監視するパスのリスト 
paths = [
  '/BusLocation/route_c/lat',
  '/BusLocation/route_n/lat',
  '/BusLocation/route_no/lat', 
  '/BusLocation/route_s/lat',
  '/BusLocation/route_no/lat',
]

# Firebaseに接続
#bus_dokoのアカウントで
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
        data=float(data)

        #初回の場合はデータを格納して終了
        if prev_data[path] is None:
            print(f'{path}: {data} 初回 \n')
            prev_data[path] = data
            time.sleep(60)

        #正常更新の場合はデータを格納して終了
        elif float(data) != prev_data[path]:
            prev_data[path] = data
            print(f'{path}: {data} 更新あり \n')
            time.sleep(60)

        #更新がない場合slackに通知
        elif float(data) == prev_data[path]:
            print(f'{path}: {data} 更新なし \n')
            requests.post(url, data = json.dumps({
                'text': f'{path}: {data} 更新なし'
            }))
            time.sleep(60)

if __name__ == '__main__':
  
  threads = []

  while True:
    for path in paths:
      t = threading.Thread(target=check_data, args=(path,))
      threads.append(t)
      t.start()
    for t in threads:
        t.join()
        time.sleep(60)
