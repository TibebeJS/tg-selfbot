from telethon import TelegramClient
from selfbot.commands import initilize

class SelfBot:
    def __init__(self, api_id, api_hash, session = "session"):
        self.client = TelegramClient(session, api_id, api_hash)
        initilize(self.client)
    def run(self):
        with self.client:
            self.client.run_until_disconnected()