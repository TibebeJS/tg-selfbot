from dotenv import load_dotenv
load_dotenv()
import os

from selfbot import SelfBot

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

if __name__ == '__main__' and __package__ is None:
    SelfBot(api_id, api_hash).run()
