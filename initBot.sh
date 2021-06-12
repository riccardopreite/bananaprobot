#!/bin/bash
TOKEN=$1
ID=$2
path="$(pwd)/$line"

python3 ~/controlBot/bot.py $TOKEN $ID
