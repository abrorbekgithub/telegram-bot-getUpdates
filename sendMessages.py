import requests
import json
from pprint import pprint

token='1690220485:AAHXCPppQIBAypOyRADaSmp3UHsH2UfOhM4'
url2=f'https://api.telegram.org/bot{token}/sendMessage'

p={
        "chat_id":1091584118,                
        "text": "salom"                             
}

res=requests.get(url=url2,params=p)
