# encoding:utf8
## closure application ##

lt = ['John','May','Winston','Harry Potter']

def filter_lt(predicate,lt):
    result = []
    for elem in lt:
        if predicate(elem):
            result.append(elem)
    return result


def len_greater_than(num):
    def len_greater_than_num(elem):
        return len(elem) > num
    return len_greater_than_num

print('大於5: ',filter_lt(len_greater_than(5),lt))
print('大於3: ',filter_lt(len_greater_than(3),lt))

print('=========================================')
print('大於5: ',filter_lt(lambda x:len(x)>5,lt))
print('大於3: ',filter_lt(lambda x:len(x)>3,lt))
