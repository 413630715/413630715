from flask import Flask, request, abort
import os
from linebot.v3 import WebhookHandler
from linebot.v3.messaging import (Configuration, ApiClient, MessagingApi,
                                  ReplyMessageRequest, TextMessage)
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from dotenv import load_dotenv

# 載入 .env 中的環境變數
load_dotenv()

app = Flask(__name__)

# 從環境變數讀取 LINE 憑證，避免把金鑰寫死在程式碼中
CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")

configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    # 取得 LINE 平台附上的簽章，用來驗證請求來源
    signature = request.headers.get('X-Line-Signature', '')
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)  # 簽章錯誤，代表不是 LINE 送來的請求

    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    # 收到文字訊息時，原封不動回覆給使用者
    with ApiClient(configuration) as api_client:
        messaging_api = MessagingApi(api_client)
        reply = ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=[TextMessage(text=event.message.text)]
        )
        messaging_api.reply_message_with_http_info(reply)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
