import csv
import requests
import json
from bs4 import BeautifulSoup as bs
import operator
import sys
import urllib
import urllib.request as ur
import json
import re
import datetime
import csv
import time
from os import system
import random
import math
from fake_useragent import UserAgent

#set user agent so they don't know this is a bot
ua = UserAgent()

#function to check price is the best and reasonable
def bestprice():
    #set random timout to not annoy the site owner
    timeout = random.randrange(60,120,1)
    #print how long it's going to wait this round
    print("-------------- " + str(timeout) + "s --------------")

    if (jobject['response'][0]['seller_login'] != "deggen"):
        betterprice = str(round(float(jobject['response'][0]['price_unit']), 0))
        announcement = "Better price found at £" + betterprice
        print(announcement)
        system("say " + announcement)
    else:
        # check price is reasonable
        myprice = float(jobject['response'][0]['price_unit'])
        theirprice = float(jobject['response'][1]['price_unit'])
        # if it's way lower - then anounce that
        if ((theirprice - myprice) >= 25.0):
            announcement = "Your offer is too low, change it to £" + str(theirprice - 26.0)
            print(announcement)
            system("say " + announcement)
        else:
            announcement = "Your offer is the best, @ £" + str(myprice) + " carry on."
            print(announcement)
    time.sleep(timeout)

# Do until I say stop
while(True):
    # set target api and fake user agent
    response = requests.get('https://bitbargain.co.uk/api/buy', headers={'User-Agent': ua.random})
    # grab the data as an object
    jobject = json.loads(response.content.decode('utf8'))
    # run the price checking function
    bestprice()
