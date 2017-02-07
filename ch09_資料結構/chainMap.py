#encoding: utf8

cust1 = {'A':'ihong','B':'elan'}
cust2 = {'C':'bayes','D':'lortz'}

custs = {}
custs.update(cust1)
custs.update(cust2)

custs

from collections import ChainMap

custs = ChainMap(cust1,cust2)
custs
custs['C']
