#! encoding:utf8

'''
implement +,-,*,/ in Rational number 
'''
class Rational:

    def __init__(self,number,denom):
        self.number = number
        self.denom = denom

    def __add__(self,that):
        return Rational(
            self.number * that.denom + that.number*self.denom,
            self.denom*that.denom
        )
    def __sub__(self,that):
        return Rational(
            self.number*that.denom - that.number*self.denom,
            self.denom*that.denom
        )

    def __mul__(self,that):
        return Rational(
            self.number * that.number,
            self.denom * that.denom
        )

    def __truediv__(self,that):
        return Rational(
            self.number * that.denom,
            self.denom * that.denom
        )
    def __str__(self):
        return '{number}/{denom}'.format(
        number=self.number,denom=self.denom)

    def __repr__(self):
        return 'Rational({number},{denom})'.format(
            number = self.number,denom=self.denom
        )

if __name__=='__main__':
    r1 = Rational(1,2)
    r2 = Rational(2,3)
    print(r1+r2)
    print(r1-r2)
    print(r1*r2)
    print(r1/r2)
    print(repr(r1))
