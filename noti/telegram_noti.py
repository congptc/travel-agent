import os
from noti.base import NotiChanel
import requests
from noti.noti_factory import NotiFactory

# Lấy API Keys từ GitHub Secrets
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

class TelegramNoti(NotiChanel):
    """
    Lớp gửi thông báo qua Telegram
    """
    def send(self, summary):
        print(f"TELEGRAM_TOKEN: {TELEGRAM_TOKEN} \n TELEGRAM_CHAT_ID: {TELEGRAM_CHAT_ID}")
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": summary, "parse_mode": "Markdown"}
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f"Lỗi gửi Telegram: {e}")
    
NotiFactory._registry["telegram"] = TelegramNoti