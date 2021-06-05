import requests as scp
import json
import time
from bs4 import BeautifulSoup
import re
inp = 0
name = input("enter name: ")
name = name.replace(' ', '%20')
lang = input("insert language: ")
ctry = input("Name of country in (MK) format: ")

def scpitemnameid():
    url = 'https://steamcommunity.com/market/listings/730/' + name
    info = scp.get(url=url).text
    soup = BeautifulSoup(info, 'lxml')
    result = re.findall(r'Market_LoadOrderSpread\(\s*(\d+)\s*\)', str(soup))
    return result[0]
def scpfromsteam():
    url = 'https://steamcommunity.com/market/priceoverview/?market_hash_name=' + name + '&appid=730&currency=3'
    info = scp.get(url=url).text
    return info
def qspriceget():
    url='https://steamcommunity.com/market/itemordershistogram'
    parameters = {
		"country": ctry,
		"language": lang,
		"currency": "3",
		"item_nameid": scpitemnameid(),
		"two_factor": "0"
    }
    info = scp.get(url=url, params=parameters)
    return info
while inp==0:
    while inp==0:
        results = scpfromsteam()
        results2 = qspriceget().text
        j2 = json.loads(results2)
        j = json.loads(results)
        qs = str(j2['buy_order_graph'][0][0]).replace('.', ',')
        print(name.replace('%20', ' '))
        print('Median price: ' + j['median_price'])
        print('sell price: ' + j['lowest_price'])
        print('quick sell price: ' + qs + '€')
        print('volume of items: ' + j['volume'])
        time.sleep(3)

