import firebase_admin
from firebase_admin import db
import time
import requests

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

LINE_API_URL = 'https://notify-api.line.me/api/notify'
LINE_API_TOKEN = os.environ['API_KEY']

#LINE送信関数
def post_message(message):
  headers = {'Authorization': 'Bearer ' + LINE_API_TOKEN}  
  data = {'message': message}
  response = requests.post(LINE_API_URL, headers=headers, data=data)
  return response.status_code == 200

while True:
  for path in paths:
    ref = db.reference(path)
    data = ref.get()
    if data == prev_data[path]:
      message = f"Error: Path {path} data has not changed"
      print(message)
	#失敗した場合LINEに送信
      if not post_message(message):
        print("Failed to send LINE notification")
    else:
      print(f"Path {path}: {data}") 
      prev_data[path] = data
  time.sleep(3600)