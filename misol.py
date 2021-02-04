import requests
import json
from pprint import pprint

token='1690220485:AAG4Tu4aA2iZJNq3w1zLD_DDo-c-RljFyQw'
def getUpdate():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    res=requests.get(url=url)
    data=res.json()
    update=data["result"]
    return update

def getText(text):
    return text

def sendMessage(idx,text):
    url=f'https://api.telegram.org/bot{token}/sendMessage'
    p={
        "chat_id":idx,
        "text":text    
    }
    r=requests.get(url=url,params=p)


length=len(getUpdate())
length_last=len(getUpdate())

while True:
    idx=getUpdate()[-1]["message"]["chat"]["id"]
    message=getUpdate()[-1]["message"]["text"]
    # text=getText(message)

    length_last=len(getUpdate())
    if length!=length_last:
        sendMessage(idx=idx,text=message)
        length=length_last

