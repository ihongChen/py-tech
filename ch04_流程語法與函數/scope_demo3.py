# encoding:utf8

x = 10

def outer():
    x= 100
    def inner():
        nonlocal x
        x =1000
    inner()
    print(x)
outer()
print(x)
