# Firebase_watch

firebaseを監視し、動きがなければslackで通知するツール

# Requirement

"hoge"を動かすのに必要なライブラリなどを列挙する

* gcloud(?)
* firebase_admin

# Installation


```bash
pip install firebase_admin
```

```Poweshell
scoop install gcloud
```

# Usage

DEMOの実行方法など、"hoge"の基本的な使い方を説明する

```bash
git clone https://github.com/kitbusstopproject/firebase_watch.git
cd firebase_watch
set GOOGLE_APPLICATION_CREDENTIALS="json_key_path"
```

# Note
認証回りでエラーおきてるっぽいのでどうにかする
```
Exception has occurred: DefaultCredentialsError
Your default credentials were not found. To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.
  File "C:\Users\tpptp\firebase_watch\main.py", line 39, in check_data
    data = db.reference(path).get()
           ^^^^^^^^^^^^^^^^^^
google.auth.exceptions.DefaultCredentialsError: Your default credentials were not found. To set up Application Default Credentials, see https://cloud.google.com/docs/authentication/external/set-up-adc for more information.
```
