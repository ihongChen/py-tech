#! -*- encoding:utf8 -*-

from collections import namedtuple

Point = namedtuple('Point',['x','y'])

p1 = Point(10,20)
print(p1)

p2 = Point(11,y=22)
p2

x,y = p1
p1.x = 1 # can't set attribute

##
lt = [10,20]
Point(*lt)

Point._make(lt)

p1._asdict()
p1._replace(x=20)

Point._fields

Point3D = namedtuple('Point3D',Point._fields + tuple('z'))

Point3D(10,20,30)

Point.__doc__ = 'Cartesian coordinate system (x,y)'
Point.x.__doc__ = 'Cartesian coordinate system x'
Point.y.__doc__ = 'Cartesian coordinate system y'

## 繼承

from math import sqrt
from collections import namedtuple

class Point(namedtuple('Point',['x','y'])):
    def len_from(self,other):
        return sqrt(pow(self.x-other.x,2) + pow(self.y - other.y,2))

p1 = Point(5,10)
p2 = Point(8,15)
p1.len_from(p2)
