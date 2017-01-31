#! encoding:utf8

class Logger:
    __loggers = {}

    def __new__(clz,name):
        if name not in clz.__loggers:
            logger = object.__new__(clz)
            clz.__loggers[name] = logger
            return logger
        return clz.__loggers[name]

    def __init__(self,name):
        if name not in vars(self):
            self.name = name

    def log(self,message):
        print('{name}:{message}'.format(name=self.name,message=message))


logger1=Logger('xlogging')
logger1.log('一些日誌訊息')
logger2=Logger('xlogging')
logger2.log('另外一些日誌訊息')
logger3=Logger('xlog')
logger3.log('再來一些日誌訊息')

print(logger1 is logger2)
print(logger1 is logger3)
