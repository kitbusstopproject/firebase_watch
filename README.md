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
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")

& $env:Temp\GoogleCloudSDKInstaller.exe
    ```

# Usage

```bash
git clone https://github.com/kitbusstopproject/firebase_watch.git
cd firebase_watch
gcloud auth application-default login
python main.py
```
