# -*- coding: utf-8 -*-
import telepot
from telepot.loop import MessageLoop
import os

from wa import Assistant

from dotenv import load_dotenv
load_dotenv()


telegram = telepot.Bot(os.getenv('TELEGRAM_TOKEN'))


def recebendoMsg(msg):

    frase = msg['text']

    assistant = Assistant()

    resp = assistant.watsonMessage(frase)

    i = 0
    for r in resp:
        i += 1
        tipoMsg, tipoChat, chatID = telepot.glance(msg)
        if tipoMsg == 'text':
            telegram.sendMessage(chatID, r)


MessageLoop(telegram, recebendoMsg).run_as_thread()

while True:
    pass
