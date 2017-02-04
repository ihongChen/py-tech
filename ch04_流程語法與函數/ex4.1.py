#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:01:25 2016

@author: ihong
"""
#%% Armstrong數 ==> 153 = 1**3 + 5**3 + 3**3
a_100s = range(1,10)
b_10s = range(0,10)
c_1s = range(0,10)
data =[]
for a in a_100s:
    for b in b_10s:
        for c in c_1s:
            if 100*a + 10*b + c == a**3 + b**3 + c**3:
                data.append(100*a + 10*b + c)
            