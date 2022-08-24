import requests 
import json
import random

def get_x_guest_token():

    ports = [9051, 9061, 9071, 9081]
    idx = random.randint(0, 3)
    port = ports[idx]
    proxies = {'http': 'socks5h://localhost:'+str(port),}    

    url_token = 'https://api.twitter.com/1.1/guest/activate.json'

    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    }
    x_guest_token = None
    try:
        x_guest_token = json.loads(requests.post(url_token, headers=headers, proxies=proxies).text)['guest_token']
    except Exception as ex:
        print(ex)
    return x_guest_token
