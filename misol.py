import requests
import json
from pprint import pprint

def getUpdate():
    url=f'https://api.telegram.org/bot{token}/getUpdates'
    res=requests.get(url=url)
    data=res.json()
    update=data["result"]
    return update

# def sendMessage():


token='1690220485:AAG4Tu4aA2iZJNq3w1zLD_DDo-c-RljFyQw'

length=len(getUpdate())
length_last=len(getUpdate())

i=0
# while True:

length_last=len(getUpdate())
print(f'{length}  {length_last}')

