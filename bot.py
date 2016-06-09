#!/usr/bin/env python
import sys
import time
import telepot
import subprocess
from time import sleep
import commands

def handle(msg):
	dict_msg = msg
	commands.__command__(dict_msg["from"]["id"], dict_msg["text"],bot)

dict_msg = dict()
#string_msg = dict()
message = ""
#user = ""

TOKEN = '233835233:AAEBsmLtNmXdbc5G811eoGuYzOIpkS1LBgk'

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)
