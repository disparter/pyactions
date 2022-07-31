# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class ManaPoolClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')


client = ManaPoolClient()
client.run(TOKEN)
