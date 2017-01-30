# coding: utf8

### 1 ####
def sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total
print(sum(1,3,5))

#### 2 #####
def account(name,number,balance):
    return {'name':name,'number':number,'balance':balance}

parameters={'name':'Justin','number':4,'balance':100}
print(account(**parameters))


##### 3  #######
def ajax(url,**user_settings):
    settings = {
        'method':user_settings.get('method','GET'),
        'contents':user_settings.get('contents',''),
        'datatype':user_settings.get('datatype','text/plain')
    }
    print('請求{}'.format(url))
    print('設定{}'.format(settings))

my_setting = {'method':'POST','contents':'book=python'}
ajax(url='http://openhome.com',**my_setting)

###### 4 #######
def some(*arg1,**arg2):
    print(arg1)
    print(arg2)

some(1,2,3)
some(a=1,b=2,c=3)
some(1,a=2,b=3)
