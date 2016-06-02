#!/usr/bin/env python

import sys
import time
import pprint
import telepot
import subprocess
import os
dict_msg = dict()
string_msg = dict()
message = ""
user = ""
def handle(msg):
	print msg
	dict_msg = msg
	print dict_msg["from"]["id"]
	if (dict_msg["from"]["id"] == 71120657):
		if dict_msg["text"] == '/up_server':
			x = os.system("up_fisso")
			if x != 0:
				bot.sendMessage(71120657, 'non ha funzionato!')
			else:
				bot.sendMessage(71120657, 'server on line a breve')
		elif dict_msg["text"] == '/reboot_board':
			x = os.system('shutdown -r 1')
			if x != 0:
				bot.sendMessage(71120657, 'non ha funzionato')
			else:
				bot.sendMessage(71120657, 'rebooting....')
		elif dict_msg["text"] == '/poweroff_board':
			x = os.system('shutdown -h `"now + 10 seconds"`')
			if x != 0:
				bot.sendMessage(71120657, 'non ha funzionato')
			else:
				bot.sendMessage(71120657, 'poweroff....')
		else:
			bot.sendMessage(dict_msg["from"]["id"], 'comando errato')
	else:
		bot.sendMessage(dict_msg["from"]["id"], 'attaccati al cazzo!!')

TOKEN = '233835233:AAEBsmLtNmXdbc5G811eoGuYzOIpkS1LBgk'

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)
