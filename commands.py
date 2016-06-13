import random
from subprocess import Popen,PIPE,STDOUT,call
import os
from time import sleep

def __command__(id,message,bot,ID):
	print ID
	dict_command = {'/pull':['cd /home/smog/bananaprobot/ && git pull && cd','bot aggiornato'],'/down_debian':['ssh smogdeb@192.168.1.10 "sudo shutdown -h"','spegnimento server debian'],'/reboot_debian':['ssh smogdeb@192.168.1.10 "sudo reboot now"','riavvio server debian'],'/up_server':['up_fisso','server on line a breve'],  '/reboot_board':['sudo shutdown -r 1','rebooting....'], '/poweroff_board':['sudo shutdown -h `"now + 10 seconds"`','poweroff....']}
	list_insulti = ['sei un cane','attaccati al cazzo','testa di minchia','gaydimmerda','fatti sfondare da un nero','porcamadonna non puoi']
	time = 5
	p = ""
	if (str(id) == ID):
		if message in dict_command.keys():
		 	proc = Popen(dict_command[message][0], shell=True, stdout=PIPE,)
			p = proc.communicate()[0]
			sleep(time/100)
			bot.sendMessage(id, p)
			bot.sendMessage(id, dict_command[message][1])
		else:
			sleep(time/100)
			bot.sendMessage(id, 'comando non previsto!')
	else:
		n = random.randint(0, 5)
		sleep(time/100)
		bot.sendMessage(id, list_insulti[n])
