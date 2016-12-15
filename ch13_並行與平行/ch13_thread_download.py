#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""利用多執行緒來下載檔案
Created on Thu Dec 15 20:54:33 2016

@author: ihong
"""


#%%

import requests
import threading
        
def download(url,file):
    res = requests.get(url)
    res.encoding = 'utf8'
    with open(file,'wb') as f:
        
        f.write(res.text.encode('utf8'))

    
urls = [
        'http://openhome.cc/Gossip/Encoding/',
        'http://openhome.cc/Gossip/Scala/',
        'http://openhome.cc/Gossip/JavaScript/',
        'http://openhome.cc/Gossip/Python/'
        ]
filenames = [
             'Encoding.html',
             'Scala.html',
             'JavaScript.html',
             'Python.html'
             ]
for url,filename in zip(urls,filenames):
    t = threading.Thread(target=download, args=(url,'./data/'+filename))
    t.start()