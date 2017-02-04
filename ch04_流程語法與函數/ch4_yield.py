# encoding:utf8
def xrange(n):
    x = 0
    while x!=n:
        yield x
        x+=1

for n in xrange(10):
    print(n)

# print xrange(10)

import sys,random

def producer():
    while True:
        data = random.randint(0,9)
        print('生產...',data)
        yield data

def consumer():
    while True:
        data = yield
        print('消費...',data)

def clerk(jobs,producer,consumer):
    print('執行 {} 次生產/消費'.format(jobs))
    p = producer()
    c = consumer()
    next(c)
    for i in range(jobs):
        data = next(p)
        c.send(data)
jobs= 3
clerk(int(jobs),producer,consumer)
# p = producer()
# c = consumer()
