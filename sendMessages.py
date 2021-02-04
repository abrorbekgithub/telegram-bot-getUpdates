import requests
import json
from pprint import pprint

def sendMessage():
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    p={
        "chat_id":1091584118,                
        "text": "salom"                             
    }
    res=requests.get(url=url,params=p)

token='1690220485:AAHXCPppQIBAypOyRADaSmp3UHsH2UfOhM4'

sendMessage()