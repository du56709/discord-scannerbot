#!/usr/bin/env python3

import discord
import asyncio

import os
import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

token = 'PUT YOUR BOT TOKEN HERE'

command_prefix = '?'

@client.event
async def on_ready():
	print(client.user.name + ' (' + str(client.user.id) + ')')

@client.event
async def on_message(msg):
	if msg.content.startswith(command_prefix + 'scan'):
		async with msg.channel.typing():
			ct = str(datetime.datetime.now().timestamp())
			# Make sure scanimage/sane works for your scanner (this took most of my time))
			os.system("scanimage --format=jpeg --output-file /usr/share/nginx/html/scans/" + ct + ".jpg --progress")
			print(ct + ".jpg")
			# So you could also setup a local nginx server and just chuck pictures on there.
			# but I think it has to be public facing for Discord to index them, so you get previews.
			await msg.channel.send('Scanned balls...', file=discord.File("/usr/share/nginx/html/scans/" + ct + ".jpg"))
			#await msg.channel.send("Scanned balls...\n" + "http://scannerbot.local/scans/" + ct + ".jpg")

client.run(token)
