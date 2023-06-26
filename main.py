import discord
import os
import openai
from bardapi import Bard
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
import config

api_key = config.BARD_API
token = os.environ['TOKEN']
openai.api_key = os.environ['OPENAI_API_KEY']
chat = ""


def bard(question):
  token = api_key
  bard = Bard(token=token)
  answer = bard.get_answer(question)['content']
  return answer.encode("utf-8")


def gpt(input):
  response = openai.Completion.create(model="text-davinci-003",
                                      prompt=input,
                                      temperature=1,
                                      max_tokens=256,
                                      top_p=1,
                                      frequency_penalty=0,
                                      presence_penalty=0)
  message = response.choices[0].text
  return message


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    global chat
    chat += f"{message.author}: {message.content} + '\n'"
    if (self.user != message.author):
      if (self.user in message.mentions):
        print(f'Message from {message.author}: {message.content}')
        channel = message.channel
        # await channel.send(gpt(f"{chat}\nAva: "))
        await channel.send(bard(f"{chat}\nAva: "))


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
