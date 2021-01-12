from telethon import TelegramClient
from dotenv import load_dotenv
load_dotenv()
import os

from commands import initilize

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
client = TelegramClient("session", api_id, api_hash)

if __name__ == '__main__' and __package__ is None:
    with client:
        initilize(client)
        client.run_until_disconnected()
