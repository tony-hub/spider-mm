#!/usr/bin/env python
# -*-coding:utf-8 -*-
__author__ = 'tony'
import urllib,urllib2
import timeit
import re
import os
from bs4 import BeautifulSoup
def spider():
    x=1
    n=0
    while x<307:
        url = 'http://www.mzitu.com/zipai/comment-page-%s/'%n
        headers = {
           # 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',

        }
        url = urllib2.Request(url,headers=headers)
        html = urllib2.urlopen(url,timeout=30).read()
        # print(html)
        # req =r'data-original="(.*?)"'
        # req = re.compile(req)
        # response = req.findall(html)
        response =BeautifulSoup(html,'html.parser').find_all('img',src=re.compile('sinaimg.cn'))
        # print(response)
        if not os.path.exists(r'D:\img'):
            os.makedirs(r'D:\img')
        for i  in response:
            n +=1
            img=i['src']
            print(img)
            print '正在保存第%s张到D盘的img文件夹'%n
            urllib.urlretrieve(img,r'D:\img\%s.%s'%(n,img.split('.')[-1]))
        x+=1
    print('爬取完毕')
if '__main__'==__name__:
    spider()
