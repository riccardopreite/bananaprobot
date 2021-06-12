import random
import os
import telepot
import socket
from time import sleep

def check_is_on(bot,ID,booting,defualt_time):
	bool = False
	if booting == True:
		time = defualt_time
		while time > 0:
			time = time - 15
			if time == 0:
				bot.sendMessage(ID, "Checking if is booted...")
			else:
				bot.sendMessage(ID, str(time) + " seconds..")
			sleep(15)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		bool = True
		s.connect(('192.168.1.80', 22))
		bot.sendMessage(ID, "System booted correctly.")
	except socket.error as e:
		bool = False
		bot.sendMessage(ID, "System not booted.")
	s.close()

	return bool

def __command__(message,bot,ID):
	dict_command = {'/onmaryjane':['etherwake E0:D5:5E:D2:CF:91 -b 192.168.1.255','turning on maryjane... 45 seconds to finish boot',45],'/nocheckon':['etherwake E0:D5:5E:D2:CF:91 -b 192.168.1.255','turning on maryjane without checking if is already booted... 45 seconds to finish boot',45], '/pingmaryjane':[' ','pinging maryjane...'],'/poweroff':['ssh root@192.168.1.80 poweroff','turning off maryjane...'],'/reboot':['ssh root@192.168.1.80 reboot','rebooting maryjane... 60 seconds to finish boot',60]}
	content_type, chat_type, chat_id = telepot.glance(message)
	print(message)
	time = 5
	if (chat_id == ID):
		if "text" in message.keys() and message['text'] in dict_command.keys():
			#IF ALREADY ON SEND A MESSAGE
			#ELSE TURNING ON PC
			if message['text'] == '/onmaryjane':
				if check_is_on(bot,ID,False,0) == False:
					os.system(dict_command[message['text']][0])
					sleep(time/100)
					bot.sendMessage(chat_id, dict_command[message['text']][1])
					sleep(15)
					check_is_on(bot,ID,True,dict_command[message['text']][2])
				else:
					bot.sendMessage(chat_id, "System already on.")

			#IF ALREADY OFF SEND A MESSAGE
			#ELSE TURNING OFF PC
			elif message['text'] == "/poweroff":
				if check_is_on(bot,ID,False,0) == True:
					os.system(dict_command[message['text']][0])
					sleep(time/100)
					bot.sendMessage(chat_id, dict_command[message['text']][1])
				else:
					bot.sendMessage(chat_id, "System already off.")

			#REBOOTING COMMAND
			elif message['text'] == '/reboot':
					os.system(dict_command[message['text']][0])
					sleep(time/100)
					bot.sendMessage(chat_id, dict_command[message['text']][1])
					sleep(15)
					check_is_on(bot,ID,True,dict_command[message['text']][2])

			#JUST PINGING MACHINE
			elif message['text'] == "/pingmaryjane":
				bot.sendMessage(chat_id, dict_command[message['text']][1])
				check_is_on(bot,ID,False,0)

			elif message['text'] == "/nocheckon":
				os.system(dict_command[message['text']][0])
				sleep(time/100)
				bot.sendMessage(chat_id, dict_command[message['text']][1])
				sleep(15)
				check_is_on(bot,ID,True,dict_command[message['text']][2])

		else:
			sleep(time/100)
			bot.sendMessage(chat_id, 'comando non previsto!')
	else:
		bot.sendMessage(chat_id,"You are not smog, get the fuck out of here.")
