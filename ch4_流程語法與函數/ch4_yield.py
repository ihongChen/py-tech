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
        print 'producing...',data
        yield data

def consumer():
    while True:
        data = yield
        print 'consuming...',data

def clerk(jobs,producer,consumer):
    print 'running {} producing/consuming'.format(jobs)
    p = producer()
    c = consumer()
    next(c)
    for i in range(jobs):
        data = next(p)
        c.send(data)

clerk(int(sys.argv[1]),producer,consumer)
p = producer()
c = consumer()
