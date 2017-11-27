from apscheduler.schedulers.blocking import BlockingScheduler
import urllib
import urllib.request as ur
import json
import re
import datetime
from bs4 import BeautifulSoup as bs
import csv


page = ur.urlopen('https://www.instagram.com/shortcutsplus/')
soup = bs(page.read(),"html.parser")
body = soup.find('body',{'class':''})
script = body.find('script',{'type':'text/javascript'})
data = json.loads(script.text.replace('window._sharedData = ', '')[:-1])
a = []

for i in range(1):
	f = open("shortcutsplus1127_1hour.csv", 'a', newline='')
	writer = csv.writer(f)
	postid = (data['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['code'])
	postDate = (data['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['date'])
	likes = (data['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['likes']['count'])
	comments = (data['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['comments']['count'])
	followers = (data['entry_data']['ProfilePage'][0]['user']['followed_by']['count'])
	follows = (data['entry_data']['ProfilePage'][0]['user']['follows']['count'])
	# a.append((postid, postDate, likes, comments))

	b = (postid, likes, comments)
writer.writerow(((datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), followers, follows,  postid, likes, comments)))
print((datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y") ,followers, follows, postid, likes, comments))
f.close()



def IG_job():
	page = ur.urlopen('https://www.instagram.com/shortcutsplus/')
	soup = bs(page.read(),"html.parser")
	body = soup.find('body',{'class':''})
	script = body.find('script',{'type':'text/javascript'})
	data = json.loads(script.text.replace('window._sharedData = ', '')[:-1])
	a = []

	for i in range(1):
		f = open("shortcutsplus1127_1hour.csv", 'a', newline='')
		writer = csv.writer(f)
		postid = (data['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['code'])
		postDate = (data['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['date'])
		likes = (data['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['likes']['count'])
		comments = (data['entry_data']['ProfilePage'][0]['user']['media']['nodes'][i]['comments']['count'])
		followers = (data['entry_data']['ProfilePage'][0]['user']['followed_by']['count'])
		follows = (data['entry_data']['ProfilePage'][0]['user']['follows']['count'])
		# a.append((postid, postDate, likes, comments))

		b = (postid, likes, comments)
	writer.writerow(((datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), followers, follows,  postid, likes, comments)))
	print((datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y") ,followers, follows, postid, likes, comments))
	f.close()

scheduler = BlockingScheduler()
scheduler.add_job(IG_job, 'interval', hours=1)
scheduler.start()
