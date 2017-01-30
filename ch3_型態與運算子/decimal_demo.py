#! encoding:utf8

import sys,decimal

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])
d1 = decimal.Decimal(sys.argv[1])
d2 = decimal.Decimal(sys.argv[2])

print('# 不使用decimal')
print('{0}+{1}={2}'.format(n1,n2,n1+n2))
print('{0}-{1}={2}'.format(n1,n2,n1-n2))
print('{0}*{1}={2}'.format(n1,n2,n1*n2))
print('{0}/{1}={2}'.format(n1,n2,n1/n2))
print('\n# 使用decimal')
print('{0}+{1}={2}'.format(d1,d2,d1+d2))
print('{0}-{1}={2}'.format(d1,d2,d1-d2))
print('{0}*{1}={2}'.format(d1,d2,d1*d2))
print('{0}/{1}={2}'.format(d1,d2,d1/d2))
