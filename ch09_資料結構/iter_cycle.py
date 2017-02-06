#encoding:utf8
import time

def cycle(elem):
    while 1:
        for e in elem:
            yield e

abcd_gen = cycle('abcd')
next(abcd_gen)

def repeat(elem,n):
    count = 0
    while count<n:
        count+=1
        yield elem

for elem in repeat('A',5):
    print(elem,end='')
