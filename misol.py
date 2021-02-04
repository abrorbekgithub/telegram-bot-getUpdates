import requests
import json
from pprint import pprint

token='1690220485:AAHXCPppQIBAypOyRADaSmp3UHsH2UfOhM4'
url=f'https://api.telegram.org/bot{token}/getUpdates'
r=requests.get(url=url)
data=r.json()
updates=data["result"]

for update in updates:
    message=update["message"]
    message_id=message["message_id"]
    pprint(message["text"])
    
#     url2=f'https://api.telegram.org/bot{token}/sendMessage'
#     p={
#         "chat_id":[ message["chat"]["id"] ] ,                
#         "text":[ message["text"] ]                             
#     }
#     res=requests.get(url=url2,params=p)
