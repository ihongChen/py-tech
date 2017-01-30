# encoding: utf-8
# print filter(lambda x:x>3, xrange(10))

def filter_lt(predicate,lt=['a','b']):
    result = []
    for elem in lt:
        if predicate(elem):
            result.append(elem)
    return result

def len_greater_than_6(elem):
    return len(elem)>6

def len_less_than_5(elem):
    return len(elem)<5

def has_i(elem):
    return 'i' in elem

lt = ['Justin','caterpillar','openhome']
print('大於6 :',filter_lt(len_greater_than_6,lt))
print('小於5 :',filter_lt(len_less_than_6,lt))
print('有個i :',filter_lt(has_i,lt))
# print len_greater_than_6(lt[1])
