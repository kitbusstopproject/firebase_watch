# Firebase_watch

firebaseを監視し、動きがなければslackで通知するツール

# Requirement

必要なライブラリ

* gcloud
* firebase-admin

# Installation


```bash
pip install firebase-admin
```

```Poweshell
scoop install gcloud
```

# Usage

```bash
git clone https://github.com/kitbusstopproject/firebase_watch.git
cd firebase_watch
gcloud auth application-default login
python main.py
```
