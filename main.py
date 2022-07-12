import discord
import requests
import asyncio
import random
from keep_alive import keep_alive
from replit import db

#get crypto data v
def getCryptoPrices(crypto):
  URL = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=php&ids=bit-castle-war&order=market_cap_desc&per_page=100&page=1&sparkline=false'
  r = requests.get(url=URL)
  data = r.json()


# putting the cryptocurrencies and their prices in db
  for i in range(len(data)):
    db[data[i]['id']] = data[i]['current_price']

  if crypto in db.keys():
    return db[crypto]
  else:
    return None

# check if a cryptocurrency is supported in this bot
def isCryptoSupported(crypto):
  if crypto in db.keys():
    return True
  else:
    return False
 
 

getCryptoPrices(0)

client = discord.Client()
quack = 'bit-castle-war'

@client.event
async def on_ready():
#status
  print('you have logged in as Miguel')

@client.event
#random status
async def ch_pr():
  await client.wait_until_ready()
  statuses = [f"B-Coin Price {getCryptoPrices(quack)} PHP",f"B-C Price {getCryptoPrices(quack)} PHP",f"B-Coin Price {getCryptoPrices(quack)} PHP",f"B-Coin Price {getCryptoPrices(quack)} PHP"]

  while not client.is_closed():
    status = random.choice(statuses)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

    await asyncio.sleep(1)

@client.event
async def on_message(message):
  if message.author == client.user:
    return

    # send crypto price directly 
  if message.content.startswith('bcw'):
    if 'bit-castle-war' in db.keys():
      await message.channel.send(f'The current price of BitCastle War Coin is: {getCryptoPrices(quack)} PHP')

  # list all the available coins
  if message.content.startswith('$list'):
    cryptoSupportedList = [key for key in db.keys()]
    await message.channel.send(cryptoSupportedList)

keep_alive()
client.loop.create_task(ch_pr())
#your discord bot token paste here 👇
client.run('')