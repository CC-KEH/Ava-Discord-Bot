import discord
import os

token = os.getenv("TOKEN")


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')
    channel = message.channel
    await channel.send("Hi! I'm Ava")


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
