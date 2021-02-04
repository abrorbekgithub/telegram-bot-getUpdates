
import requests
import json
from pprint import pprint

token='1690220485:AAHXCPppQIBAypOyRADaSmp3UHsH2UfOhM4'
url1=f'https://api.telegram.org/bot{token}/getUpdates'
r=requests.get(url=url1)
data1=r.json()


updates=data1["result"]


delivered=100


while True:    
    if msg_id>delivered:
        msg_id=updates[i]["message"]["message_id"]
        url2=f'https://api.telegram.org/bot{token}/sendMessage'
        p={
        "chat_id":[ updates[i]["message"]["chat"]["id"] ],
        "text":[ updates[i]["message"]["text"] ]
        }
        msg_id=updates[i]["message"]["message_id"] 
        res=requests.get(url=url2,params=p)
        delivered=msg_id


 


