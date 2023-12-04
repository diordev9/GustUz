import requests
from environs import Env

env = Env()
env.read_env()


class BotSendToUser:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id

    def send_message(self, text):
        url = f"https://api.telegram.org/bot{self.token}/sendMessage"
        params = {
            "chat_id": self.chat_id,
            "text": text,
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return True
        return False, response.json()

    def send_document(self, file_path):
        url = f"https://api.telegram.org/bot{self.token}/sendDocument"
        f = open(file_path, "rb")
        file_byte = f.read()
        f.close()
        params = {
            "chat_id": self.chat_id,
        }
        response = requests.post(
            url, params=params, files={"document": (f.name, file_byte)}
        )
        if response.status_code == 200:
            return (True,)
        return False, response.json()


bot = BotSendToUser(env.str("BOT_TOKEN"), env.str("CHAT_ID"))
