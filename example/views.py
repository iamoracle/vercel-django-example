from datetime import datetime

from django.http import JsonResponse

import requests


def index(request):
    
    response = requests.get("https://www.dextools.io/chain-bsc/api/pancakeswap/poolx?pairSelected=0x07ddae60a99421eb948ae5f299117f8f8fe86a66")
   
    return JsonResponse(response.json())
