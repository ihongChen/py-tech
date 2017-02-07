#! -*- encoding:utf8 -*-

from collections import defaultdict,Counter

names = ['ihong','Monica','obvyah','heloha','hihi']

grouped_by_len = defaultdict(list)

for name in names:
    key = len(name)
    grouped_by_len[key].append(name)

for length in grouped_by_len:
    print(length,grouped_by_len[length])

c1 = Counter(['hi','hi','hello','hello'])
c1
for e in c1.elements():
    print(e)
