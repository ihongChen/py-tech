#! encoding:utf8

# usage: map_lt(str.upper,lt) ==> [PETER,JOHN,]

def map_lt(mapper,lt):
    result = []
    for elem in lt:
        result.append(mapper(elem))
    return result

lt  = ['peter','john','michael']

print(map_lt(str.upper,lt))
print(map_lt(len,lt))
