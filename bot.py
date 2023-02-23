import sys
import discord
from discord.ext import commands

import openai

from dotenv import load_dotenv
import os

load_dotenv()
# print(os.environ["API_KEY"])
# print(os.environ["DC_API_KEY"])

# openai.api_key = sys.argv[1]
openai.api_key = os.environ["OPEN_AI_API_KEY"]

def generate_response(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message

# while True:
#   user_input = input("> ")
#   if user_input == "exit":
#     break

#   response = generate_response(user_input)
#   print(response)


client = commands.Bot(intents=discord.Intents.all() ,command_prefix= '.')

@client.event
async def on_ready():
    print('Bot is ready')
    # await client.change_presence(status=discord.Status.online, activity=discord.CustomActivity(name='Custom Status',emoji='🙃', state = 'dfg'))
    # await client.change_presence(activity= discord.Activity(name="Test",type=-1, details= 'jj', state = 'state'))
    print('client', client.user)



@client.command()
async def ping(ctx):
    print(ctx)
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

# greets = ['hi', 'hola', 'hello']

@client.event
async def on_message(message):
    msg = message.content.lower()
    checkmsg = message.content[:6].lower()
    # print(checkmsg)
    # sys.stdout.flush(checkmsg)
    if(checkmsg.startswith('!atia ') and message.author !=  client.user):
        # print(message.content[6:])
        
#         if(("your" in msg) and ("name" in msg) ):
#           await message.channel.send("My name is ATIA(Advanced Thinking and Intelligent Assistance).")
#         elif(("your" in msg) and ("developer" or "creator" in msg) ):
#           await message.channel.send("This discord chat-bot is developed by Shashank J..")
        else:
          res = generate_response(message.content)
          print(res)
          await message.channel.send(res)
    # for greet in greets:
    #     if((greet in message.content.lower()) and ( message.author !=  client.user)):
    #         await message.channel.send(f'Hello {message.author}')

    # if ('greet' in message.content.lower()):
    #     channel = message.channel
    #     await channel.send('Say hello!')

    #     def check(m):
    #         return m.content == 'hello' and m.channel == channel

    #     msg = await client.wait_for('message', check=check)
    #     await channel.send(f'Hello {msg.author}!')

print('client', client.user)
# client.run(sys.argv[2])
client.run(os.environ["DC_API_KEY"])
