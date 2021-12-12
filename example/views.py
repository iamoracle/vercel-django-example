from datetime import datetime

from django.http import JsonResponse

import requests

import random

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

url = 'https://httpbin.org/headers'

#Pick a random user agent
user_agent = random.choice(user_agent_list)

#Set the headers 
headers = {'User-Agent': user_agent}

def index(request):
    
    response = requests.get("https://www.dextools.io/chain-bsc/api/pancakeswap/poolx?pairSelected=0x07ddae60a99421eb948ae5f299117f8f8fe86a66", headers=headers)
   
    return JsonResponse(response.json())

def price(request):
    
    from datetime import datetime
    
    timestamp = str(int(datetime.now().timestamp()))
    
    response = requests.get("https://www.dextools.io/chain-bsc/api/pancakeswap/1/pairexplorer?v=1.22.8&pair=0x07ddae60a99421eb948ae5f299117f8f8fe86a66&ts=" + timestamp, headers=headers)
   
    return JsonResponse(response.json())
