from noti.base import NotiChanel
import requests
from noti.noti_factory import NotiFactory

# Lấy API Keys
TELEGRAM_TOKEN = "8317590907:AAEBwNRwFyjF7eug-WUPFu3d4ovHC9DSkhU"
TELEGRAM_CHAT_ID = "-5101173330"

class MockNoti(NotiChanel):
    """
    Lớp gửi thông báo qua Telegram
    """
    def send(self, summary):
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {"chat_id": TELEGRAM_CHAT_ID, "text": summary, "parse_mode": "Markdown"}
        try:
            requests.post(url, json=payload)
        except Exception as e:
            print(f"Lỗi gửi Telegram: {e}")
    
NotiFactory._registry["mock"] = MockNoti