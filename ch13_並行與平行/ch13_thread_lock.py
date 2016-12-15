#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 21:33:06 2016

@author: ihong
"""


import threading 

#%% 競速race
def setTo1(data):
    while 1 :
        data['chen'] = 1
        if data['chen'] != 1:
            raise ValueError('setTo1 資料不一致:{}'.format(str(data)))
            
def setTo2(data):
    while 1 :
        data['chen'] = 2
        if data['chen'] != 2 :
            raise ValueError('setTo2 資料不一致:{}'.format(str(data)))
data = {}        
t1 = threading.Thread(target=setTo1,args=(data,))
t2 = threading.Thread(target=setTo2,args=(data,))

t1.start()
t2.start()


#%% 必須利用鎖定(Lock)

def setTo1(data,lock):
    while 1:
        with lock:
            data['chen'] = 1
            if data['chen'] != 1 :
                raise ValueError('setTo1 資料不一致:{}'.format(str(data)))
                
def setTo2(data,lock):
    while 1 :
        with lock:
            data['chen'] = 2
            if data['chen'] != 2 :
                raise ValueError('setTo2 資料不一致:{}'.format(str(data)))

data = {}
lock = threading.Lock()
t1 = threading.Thread(target=setTo1,args=(data,lock))
t2 = threading.Thread(target=setTo2,args=(data,lock))

t1.start()
t2.start()

# ps.使用lock需要小心死結...(你不解開lock我就不放開lock....)