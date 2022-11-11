import requests

ETH_API_KEY = ''
ARB_API_KEY = ''
BSC_API_KEY = ''
POL_API_KEY = ''

def blockNumberETH(time, place):
    bp = {
        "module": 'block',
        "action": 'getblocknobytime',
        "timestamp": time,
        "closest": place,
        "apikey": ETH_API_KEY
    }

    response = requests.get('https://api.etherscan.io/api?', params=bp)
    response.raise_for_status()
    block = response.json()['result']
    print(block)
    return block

def blockNumberARB(time, place):
    bp = {
        "module": 'block',
        "action": 'getblocknobytime',
        "timestamp": time,
        "closest": place,
        "apikey": ARB_API_KEY
    }

    response = requests.get('https://api.arbiscan.io/api?', params=bp)
    response.raise_for_status()
    block = response.json()['result']
    print(block)
    return block

def blockNumberBSC(time, place):
    bp = {
        "module": 'block',
        "action": 'getblocknobytime',
        "timestamp": time,
        "closest": place,
        "apikey": BSC_API_KEY
    }

    response = requests.get('https://api.bscscan.com/api?', params=bp)
    response.raise_for_status()
    block = response.json()['result']
    print(block)
    return block

def blockNumberPOL(time, place):
    bp = {
        "module": 'block',
        "action": 'getblocknobytime',
        "timestamp": time,
        "closest": place,
        "apikey": POL_API_KEY
    }

    response = requests.get('https://api.polygonscan.com/api?', params=bp)
    response.raise_for_status()
    block = response.json()['result']
    print(block)
    return block

