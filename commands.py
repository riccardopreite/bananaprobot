import random
from subprocess import Popen,PIPE,STDOUT,call
import os
from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port

import dht11
import time
import datetime
import telepot
import speech_recognition as sr
from pathlib import Path
import subprocess


def temperature():
    PIN = port.PA6
    gpio.init()
    instance = dht11.DHT11(pin=PIN)
    
    while True:
        result = instance.read()
        if result.is_valid():
            return("date: {}  Temperature: {}C and Humidity: {}%".format(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), result.temperature, result.humidity))


def __command__(message,bot,ID):
    r = sr.Recognizer()
    dict_command = {'/temperature': temperature()}
    list_insulti = ['sei un cane','attaccati al cazzo','testa di minchia','gaydimmerda','fatti sfondare da un nero','porcamadonna non puoi']
    time = 5
    to_send = ""
    content_type, chat_type, chat_id = telepot.glance(message) 
    print("message format: ", message)
    print("content_type: ", content_type, "chat_type: ", chat_type, "chat_id: ",chat_id)
    if (chat_id == ID) or True:
        if "text" in message.keys() and message['text'] in dict_command.keys():
            to_send = dict_command[message['text']]
            sleep(time/100)
            bot.sendMessage(chat_id, to_send)
        elif content_type=="voice":
            file_name = message['voice']['file_id']
            bot.download_file(message['voice']['file_id'],"{0}.ogg".format(file_name)) 
            audio=Path("./{0}.ogg".format(message['voice']['file_id']))
            shell_cmd = "yes y | ffmpeg -i {0}  {1}.wav".format(audio,file_name)
            p = subprocess.Popen(shell_cmd, shell=True,stdout=subprocess.PIPE)
            while(p.wait() != 0):
                time.sleep(2)
            audio=sr.AudioFile(file_name+'.wav')
            with audio as source:
                audio=r.record(source)
            bot.sendMessage(chat_id, r.recognize_google(audio, language='it-IT'))
    else:
        n = random.randint(0, 5)
        sleep(time/100)
        bot.sendMessage(chat_id, list_insulti[n])
