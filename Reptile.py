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

GOOGLE_TREND_API = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed={}&geo=TW&ns=15'

# https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&ed=20200507&geo=TW&ns=15

def renew(date):
    response = requests.get(GOOGLE_TREND_API.format(date))
    Tmp = response.text

    Tmp = json.loads(Tmp.replace(')]}\',\n', ''))

    data = Tmp['default']['trendingSearchesDays'][0]['trendingSearches']
    print 'data length: {}'.format(len(data))

    for i in range(0, len(data)):
    # for i in range(0, 1)
        try:
            firstArticle = data[i]['articles'][0]
            print firstArticle['url']
            print firstArticle['title']
            firstUrl = firstArticle['url']
            
            response = requests.get(firstUrl)
            # print 'success'
            soup = BeautifulSoup(response.text, 'lxml')
            
            imgUrl = soup.find("meta", property="og:image")['content']
            print imgUrl
            imageList.append({'img':imgUrl, 'url':firstUrl, 'title':firstArticle['title']})
        except Exception as e:
            print e

    # print imageList

while 1:
    imageList = []
    for i in range( 0, 3 ):
        date = (datetime.now() - timedelta(i)).strftime('%Y%m%d')
        renew(date)

    jsString = 'var imageList = {};'.format(json.dumps(imageList))

    with open( 'data.js', "w" ) as text_file:
        text_file.write(jsString)

    print 'end'

    time.sleep(3600)