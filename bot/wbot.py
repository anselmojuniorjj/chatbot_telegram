# -*- coding: utf-8 -*-
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import telepot
from telepot.loop import MessageLoop
import os
from dotenv import load_dotenv
load_dotenv()


# authenticator = IAMAuthenticator('njyivfAVLyznXwryzdRrNBIH5tO5rGaVO4W_TNxFnapg')
authenticator = IAMAuthenticator(os.getenv('API_KEY'))

service = AssistantV1(
    version='2019-02-08',
    authenticator=authenticator
)

service.set_service_url('https://gateway.watsonplatform.net/assistant/api')

# telegram = telepot.Bot("896415169:AAF-m60qjYm2WYFh36lpS8EWpiIbgn5CZ84")
telegram = telepot.Bot(os.getenv('TELEGRAM_TOKEN'))

context = {}


def recebendoMsg(msg):

    frase = msg['text']

    if context is not None:

        response = service.message(
            workspace_id=os.getenv('WORKSPACE_ID'),
            input={
                'text': frase
            },
            context=context
        ).get_result()

        resp = response.get('output').get('text')

        i = 0
        for r in resp:
            i += 1
            tipoMsg, tipoChat, chatID = telepot.glance(msg)
            if tipoMsg == 'text':
                telegram.sendMessage(chatID, r)

    else:
        response = service.message(
            workspace_id=os.getenv('WORKSPACE_ID'),
            input={
                'text': frase
            }
        ).get_result()

        resp = response.get('output').get('text')

        i = 0
        for r in resp:
            i += 1
            tipoMsg, tipoChat, chatID = telepot.glance(msg)
            if tipoMsg == 'text':
                telegram.sendMessage(chatID, r)

    def change_context():
        global context
        context = response.get('context')

    change_context()

    # tipoMsg, tipoChat, chatID = telepot.glance(msg)
    # if tipoMsg == 'text':
    #     telegram.sendMessage(chatID, resposta)


MessageLoop(telegram, recebendoMsg).run_as_thread()

while True:
    pass