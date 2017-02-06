#encoding:utf8

class Customer:
    def __init__(self,name,symbol,age):
        self.name = name
        self.symbol = symbol
        self.age = age

    def __lt__(self,other):
        return self.name <other.name

    def __str__(self):
        return "Customer('{name}','{symbol}',{age})".format(**vars(self))
    def __repr__(self):
        return self.__str__()

customers = [
    Customer('Jack','A',40),
    Customer('Ireane','C',8),
    Customer('Monica','B',36)
]

print(sorted(customers))
print(sorted(customers,key=lambda object:object.name))

from operator import itemgetter,attrgetter

sorted(customers,key=attrgetter('name'))

customers2 = [
    ('Justin','A',40),
    ('Monica','B',30),
    ('Jack','C',38)
]
sorted(customers2,key=itemgetter(0))
