#appid: 1122565355143958530
#publickey: dee134e1d66d6bca2e2e13cdfbc45b655ad24a0da01b68fb3b91c8c50ac483c0
#MTEyMjU2NTM1NTE0Mzk1ODUzMA.GMiwxu.ZQXgjpIZ33oqMals8cabpLRP2qyUcm82nZLd5Y
#https://discord.com/api/oauth2/authorize?client_id=1122565355143958530&permissions=4398083214336&scope=bot

import discord


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')
