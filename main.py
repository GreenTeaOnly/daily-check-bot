from dotenv import load_dotenv
import discord
import os
load_dotenv()

# This example requires the 'message_content' intent.
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_BOT_TOKEN'))
