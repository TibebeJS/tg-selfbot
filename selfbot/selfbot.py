from telethon import TelegramClient
from selfbot import commands

class SelfBot:
    def __init__(self, api_id, api_hash, session = "session"):
        self.client = TelegramClient(f'./KEEP_SECRET/{session}', api_id, api_hash)
        self.active_commands = []
        self.initilize()

    def initilize(self):
        self.client.start()
        self.activateCommand(commands.ls(self))
        self.activateCommand(commands.helper(self))
        # self.activateCommand(commands.rm(self)) # not ready for use yet.
        self.client.loop.run_until_complete(self.client.send_message("me", "`[✓] Bot is up and running...`\n\nsend `.help` to see available commands"))

    def activateCommand(self, command):
        self.active_commands.append(command)

    def run(self):
        self.client.run_until_disconnected()