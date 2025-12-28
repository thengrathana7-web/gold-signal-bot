import os
from flask import Flask, request
import requests

app = Flask(__name__)

# ព័ត៌មានដែលអ្នកបានផ្ដល់ឱ្យ
TELEGRAM_TOKEN = '8034462235:AAF8zB2HolA06mydI36xmeZHIGyHTbbA42Y'
CHAT_ID = '8056179793'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data:
        # រៀបចំសារសម្រាប់ផ្ញើទៅ Telegram
        msg = f"🔔 *GOLD SIGNAL ALERT*\n" \
              f"━━━━━━━━━━━━\n" \
              f"📈 Action: *{data.get('action')}*\n" \
              f"💰 Price: {data.get('price')}\n" \
              f"🎯 TP: {data.get('tp')}\n" \
              f"🛑 SL: {data.get('sl')}\n" \
              f"━━━━━━━━━━━━"
        send_telegram_message(msg)
    return 'OK', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)