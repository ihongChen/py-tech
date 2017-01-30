# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:19:44 2016

@author: ihong
"""

# In[]: 9.1.1 hashable協定

#{[1,2,3]} # Type Error
#{{'1':1}}
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'point({},{})'.format(self.x,self.y)
        
p1 = Point(1,1)
p2 = Point(2,2)
p3 = Point(1,1)

ps = {p1,p2,p3}
print(ps)
# In[2] 
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self,that):
        if hasattr(that,'x') and hasattr(that,'y'):
            return self.x == that.x and self.y == that.y
            
        return False
    def __hash__(self):
        return 41*(41+self.x) + self.y
        
    def __str__(self):
        return self__repr__()
        
    def __repr__(self):
        return 'Point({},{})'.format(self.x,self.y)
        
p1 = Point(1,1)
p2 = Point(2,2)
p3 = Point(1,1)

ps = {p1,p2,p3}
print(ps)

# In[3]
def cycle(elems):
    for elem in elems:
        while True:
            for elem in elems:
                yield elem
abcd_gen = cycle('abcd')
print(next(abcd_gen))
print(next(abcd_gen))
print(next(abcd_gen))
print(next(abcd_gen))
print(next(abcd_gen))

# In[4] 實做__iter__()

class Repeat: #py2不work!!!
    
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
                if self.count < n:
                    self.count+=1 
                    return elem
                else:
                    raise StopIteration
                    
            def __iter__(self):
                return self
        return _Iter() # 傳回迭代器實例
        
#for e in Repeat('A',5):
#    print e

temp = Repeat('A',5)
next(temp)






