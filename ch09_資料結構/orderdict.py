#! -*- encoding:utf8 -*-

from collections import OrderedDict

custs = [
    ('A','ihongChen'),
    ('B','obvyah'),
    ('C','alfred')
]

cust_dict = OrderedDict(custs)

for key in cust_dict:
    print(key,':',cust_dict[key])


##
from operator import itemgetter

origin_dict = {'A':85,'B':90,'C':70}
sort_dict = sorted(origin_dict.items(),key=itemgetter(0))
OrderedDict(sort_dict)

sort_dict2 = sorted(origin_dict.items(),key=itemgetter(1))
OrderedDict(sort_dict2)
