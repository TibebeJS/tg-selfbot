from telethon import TelegramClient
from selfbot import commands

class SelfBot:
    def __init__(self, api_id, api_hash, session = "session"):
        self.client = TelegramClient(session, api_id, api_hash)
        self.active_commands = []
        self.initilize()

    def initilize(self):
        self.activateCommand(commands.ls(self))
        self.activateCommand(commands.helper(self))
        # self.activateCommand(commands.rm(self)) # not ready for use yet.

    def activateCommand(self, command):
        self.active_commands.append(command)

    def run(self):
        with self.client:
            self.client.run_until_disconnected()