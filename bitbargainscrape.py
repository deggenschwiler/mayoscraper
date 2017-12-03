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

from fake_useragent import UserAgent
ua = UserAgent()

goood = True

def isitme(userMe):
    line = []
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            line.append(str(cell.getText().strip().replace(" ", "")))
            while(userMe == True):
                if (str(cell.getText().strip().replace(" ", "")) != "deggen"):
                    userMe = False
                    global goood
                    goood = False
                else:
                    timeout = random.randrange(60,120,1)
                    print("-------------- " + str(timeout) + "s --------------")
                    time.sleep(timeout)
                    return "Your offer is the best one."
    print lune[18]
    return line[4]

while(goood):
    request = requests.get('https://bitbargain.co.uk/buy', headers={'User-Agent': ua.random})
    content = request.content
    soup = bs(content, 'html.parser')
    table = soup.findChildren('table')[1]
    rows = table.findChildren('tr')
    isit = isitme(True)
    print(isit)
sagen = "say Price dropped to " + isit
system(sagen)
