#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""執行緒的join/停止方法
Created on Thu Dec 15 21:14:55 2016

@author: ihong
"""

#%% 加入join 用法

import threading,time

def demo():
    print('Thread B 開始')
    for i in range(5):
        print('Thread B 執行中...')
    print('Thread B 即將結束')

print('Main Thread開始')    
th = threading.Thread(target = demo)
th.start()
th.join(10) # 比較沒有這行的結果

print('Main Thread 將結束...')

#%% 停止執行緒

class Some:
    
    def __init__(self):
        self.is_continue = True
        
    def terminate(self):
        self.is_continue =False
        
    def run(self):
        while self.is_continue:
            print('running....running...')

s = Some()
t = threading.Thread(target=s.run)
t.start()
time.sleep(1)
s.terminate()


