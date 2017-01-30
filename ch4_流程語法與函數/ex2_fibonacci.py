# encoding:utf8

# a = int(input('Give amount: '))
a = 20
def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

print(list(fib(a)))
