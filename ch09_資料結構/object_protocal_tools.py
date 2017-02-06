#encoding:utf8

class Repeat:
    def __init__(self,elem,n):
        self.elem = elem
        self.n = n

    def __iter__(self):
        elem = self.elem
        n = self.n

        class _Iter:
            def __init__(self):
                self.count = 0
            def __next__(self):
                if self.count <n:
                    self.count +=1
                    return elem
                else:
                    raise StopIteration
            def __iter__(self):
                return self
        return _Iter()

for elem in Repeat('A',5):
    print(elem,end='')
