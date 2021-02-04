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

token='1690220485:AAG4Tu4aA2iZJNq3w1zLD_DDo-c-RljFyQw'

sendMessage()