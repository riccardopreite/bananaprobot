#!/bin/bash
TOKEN=$1
ID=$2
path="$(pwd)/$line"

python3 /home/smog/controlBot/bot.py $TOKEN $ID
