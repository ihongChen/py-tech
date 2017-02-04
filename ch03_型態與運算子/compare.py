#! encoding=utf8

import sys

str1 = sys.argv[1]
str2 = sys.argv[2]

print('"{}" >"{}" ? {}'.format(str1,str2,str1>str2))
print('"{}" =="{}" ? {}'.format(str1,str2,str1==str2))
print('"{}" <"{}" ? {}'.format(str1,str2,str1<str2))
