#encoding:utf8

import itertools

cycle_gen = itertools.cycle('abcd')
next(cycle_gen)

rept_gen = itertools.repeat('A',10)
list(rept_gen)

list(itertools.accumulate([1,2,3,4,5]))

list(itertools.accumulate([1,2,3,4,5],int.__mul__))

list(itertools.chain('ABC',[1,2,3]))
list(itertools.chain.from_iterable([[8,1,7],[1,2,3],['a','b']]))

list(itertools.dropwhile(lambda x:x<5,[1,4,6,4,1]))
list(itertools.takewhile(lambda x:x<5,[1,4,6,4,1]))

list(itertools.filterfalse(lambda x:x%2,[1,2,3,4]))

names = ['ihong','obvyah','monica','anyu','caterpillar']
group_by_name = itertools.groupby(names,lambda name:len(name))

for length,group in group_by_name:
    print(length,list(group))
