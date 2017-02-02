#! encoding: utf8

def natural():
    n = 0

    try:
        while True:
            n +=1
            yield n
    except GeneratorExit:
        print('GeneratorExit',n)

n=natural()
next(n)
next(n)
n.close()
