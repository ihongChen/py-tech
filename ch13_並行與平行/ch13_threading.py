#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" 利用執行緒的概念實現龜兔賽跑
Created on Wed Dec 14 22:19:55 2016

@author: ihong
"""
# In[]
import threading,random, time

def totrise(total_step):
    step = 0 
    while step < total_step:
        step += 1        
        print('烏龜跑了{}步...'.format(step))
        time.sleep(0.1)

def hare(total_step):
    step = 0
    flag = [True,False]
    while step < total_step:
        sleeping = flag[random.randint(0,1)]
        if sleeping:
            print('兔子睡著了zzz...')
            time.sleep(0.1)
        else:
            step += 2
            print('兔子跑了{}步...'.format(step))
            time.sleep(0.1)
            
t = threading.Thread(target=totrise, args=(10,)) # 建立thread實例
h = threading.Thread(target=hare, args=(10,))

t.start()
h.start()


#%% 
## 繼承寫法

class Tortoise(threading.Thread):
    def __init__(self,total_step):
        super().__init__()
        self.total_step = total_step
        
    def run(self):
        step = 0
        while step < self.total_step:
            step += 1 
            print('烏龜跑了{}步'.format(step))
            
class Hare(threading.Thread):
    def __init__(self,total_step):
        super().__init__()
        self.total_step = total_step
        
    def run(self):
        step = 0
        flags = [True,False]
        while step < self.total_step:
            sleeping = flags[random.randint(0,1)]
            if sleeping :
                print('兔子睡著了')
            else:
                step +=2 
                print('兔子跑了{}步'.format(step))
                
Tortoise(10).start()
Hare(10).start()
        
            
        
        
        
        
        