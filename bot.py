#!/usr/bin/env python
import sys
import time
import telepot
import subprocess
from time import sleep
import commands

def handle(msg):
	commands.__command__(msg, bot, int(ID))

dict_msg = dict()
string_msg = dict()
message = ""
user = ""

TOKEN = sys.argv[1]
ID = sys.argv[2]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)

print ('Listening ...')
bot.sendMessage(ID,"Turned on smogBot")
# Keep the program running.
while 1:
	time.sleep(10)

