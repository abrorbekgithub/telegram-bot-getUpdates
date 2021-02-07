import requests
import json
from pprint import pprint

def getUpdate():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    r=requests.get(url=url)
    data=r.json()
    updates=data["result"]
    return updates

    

token='1690220485:AAFtkQoAYsn2FQ-UqzqRSxWk-WlHitTbWo0'


for update in getUpdate():
    message=update["message"]
    chat_id=message["chat"]["id"]
    text=message.get("text","entities")
    print(chat_id)


