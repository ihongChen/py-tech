#encoding: utf8

def a():
    text = None
    return text.upper() # exception

def b():
    a()

def c():
    b()

try:
    c()
except:
    import traceback
    traceback.print_exc()
    # traceback.print_exc(file=open('traceback.txt','w+')) ## 寫入檔案
