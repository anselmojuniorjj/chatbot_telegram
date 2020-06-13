# -*- coding: utf-8 -*-
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os

from dotenv import load_dotenv
load_dotenv()

class Assistant():
	
    context = {}

    def watsonMessage(self, msg):
        
        
        authenticator = IAMAuthenticator(os.getenv('API_KEY'))

        service = AssistantV1(
            version='2019-02-08',
            authenticator=authenticator
        )

        service.set_service_url('https://gateway.watsonplatform.net/assistant/api')

        frase = msg

        if 'context' in globals() and context is not None:
            response = service.message(
                    workspace_id=os.getenv('WORKSPACE_ID'),
                    input={
                        'text': frase
                    },
                    context=context                    
                ).get_result()                    
        else:
            response = service.message(
                    workspace_id=os.getenv('WORKSPACE_ID'),
                    input={
                        'text': frase
                    }
                ).get_result()                        

        resp = response.get('output').get('text')        

        def change_context():
            global context
            context = response.get('context')
        change_context()        

        return resp
