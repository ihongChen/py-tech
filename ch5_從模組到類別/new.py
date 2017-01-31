#! encoding:utf8

class Some:

    def __new__(clz,isClzInstance):
        print('__new__')
        if isClzInstance:
            return object.__new__(clz)
        else:
            return None

    def __init__(self,isClzInstance):
        print('__init__')
        print(isClzInstance)
Some(True)

Some(False)
print(Some(False))
