# LINE Messaging API Echo Bot

本專案示範使用 Python、Flask 與 LINE Bot SDK v3 建立 LINE Echo Bot。

## 安裝

```powershell
python -m pip install -r requirements.txt
```

建立 `.env`，填入 LINE Developers Console 的憑證：

```text
LINE_CHANNEL_SECRET=你的ChannelSecret
LINE_CHANNEL_ACCESS_TOKEN=你的ChannelAccessToken
```

## 啟動

```powershell
python app.py
```

程式預設監聽 `http://localhost:8000`，本機測試時可使用 ngrok 建立 HTTPS Webhook，並將網址設定為 `/callback`。

## 文件

- `main.tex`：LaTeX 教學文件原始碼
- `main.pdf`：編譯後的教學文件
- `app.py`：Flask LINE Echo Bot
