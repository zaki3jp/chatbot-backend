from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.exceptions import InvalidSignatureError
from flask import Flask, request, abort

app = Flask(__name__)

line_bot_api = LineBotApi('2004489777')
handler = WebhookHandler('582e8359cf2bb66b99dce532dcda60c0')

@app.route("/callback", methods=['POST'])
def callback():
 signature = request.headers['X-Line-Signature']
body = request.get_data(as_text=True)
try:
 handler.handle(body, signature)
except
    InvalidSignatureError:
        abort(400)
        return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
 if '参加しました' in event.message.text:
  line_bot_api.reply_message(
event.reply_token,
TextSendMessage(text='ようこそ 科学部へ！')
)

if __name__ == "__main__":
  app.run()
