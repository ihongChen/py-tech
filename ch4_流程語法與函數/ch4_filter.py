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

def len_less_than_6(elem):
    return len(elem)<5

def has_i(elem):
    return 'i' in elem

lt = ['Justin','caterpillar','openhome']
print filter_lt(len_greater_than_6,lt)
# print len_greater_than_6(lt[1])
