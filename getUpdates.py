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
    firstname=message["from"]["first_name"]
    pprint(firstname)