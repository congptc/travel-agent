import os
from noti.base import NotiChanel
import requests
from noti.noti_factory import NotiFactory


class TelegramNoti(NotiChanel):
    """
    Lớp gửi thông báo qua Telegram
    """

    def __init__(self):
    # Nạp Key ngay khi đối tượng được tạo ra
        self.telegram_token = os.getenv("TELEGRAM_TOKEN")
        self.telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if not self.telegram_token or not self.telegram_chat_id  :
            raise ValueError("LỖI: Không tìm thấy TELEGRAM_TOKEN hoặc TELEGRAM_CHAT_ID  trên GitHub Secrets!")

    def send(self, summary):
        url = f"https://api.telegram.org/bot{self.telegram_token}/sendMessage"
        payload = {"chat_id": self.telegram_chat_id, "text": summary, "parse_mode": "MarkdownV2"}
        print(f"Địa chỉ telegram: {url}")
        print(f"Telegram có chạy đến đây ko: {summary}")
        try:
            response= requests.post(url, json=payload)
            print("STATUS CODE:", response.status_code)
            print("RESPONSE OK?:", response.ok)
        
        except Exception as e:
            print(f"Lỗi gửi Telegram: {e}")
    
NotiFactory._registry["telegram"] = TelegramNoti
