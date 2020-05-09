# coding=UTF-8

import os
import sys
import json 
import time
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter

reload(sys)
sys.setdefaultencoding("utf-8")

GOOGLE_TREND_API = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&geo=TW&ns=15'

response = requests.get(GOOGLE_TREND_API)

Tmp = response.text

Tmp = json.loads(Tmp.replace(')]}\',\n', ''))

data = Tmp['default']['trendingSearchesDays'][0]['trendingSearches']
print 'data length: {}'.format(len(data))

imageList = []

for i in range(0, len(data)):
# for i in range(0, 1):
    firstArticle = data[i]['articles'][1]
    print firstArticle['url']
    print firstArticle['title']
    firstUrl = firstArticle['url']
    
    response = requests.get(firstUrl)
    print 'success'
    soup = BeautifulSoup(response.text, 'lxml')
    imgUrl = soup.find("meta", property="og:image")['content']
    print imgUrl
    imageList.append({'img':imgUrl, 'url':firstUrl, 'title':firstArticle['title']})

print imageList

jsString = 'var imageList = {};'.format(json.dumps(imageList))

with open( 'data.js', "w" ) as text_file:
    text_file.write(jsString)