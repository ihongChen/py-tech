#! ecnoding:utf8
'''
強制子類別必須實做fight方法
'''
from abc import ABCMeta, abstractmethod

class Role(metaclass=ABCMeta):

    def __init__(self,name,level,blood):
        self.name = name
        self.level = level
        self.blood = blood

    @abstractmethod
    def fight(self):
        pass

    def __str__(self):
        return "('{name}',{level},{blood})".format(**vars(self))

    def __repr__(self):
        return self.__str__

class SwordsMan(Role):
    def fight(self):
        print('揮劍攻擊')
    def __str__(self):
        return 'SwordsMan' + super().__str__()

class Magician(Role):
    def fight(self):
        print('魔法攻擊')

    def cure(self):
        print('魔法治療')

    def __str__(self):
        return 'Magician' + super().__str__()

class Monster(Role):
    def __str__(self):
        return 'Monster' + super().__str__()

if __name__ =='__main__':
    swordsman = SwordsMan('Justin',1,200)
    print(swordsman)
    magician = Magician('Monica',1,100)
    print(magician)

    Role('ihong',1,200) ## Err, 因為沒有實做fight方法
    monster = Monster('ET',1,50) ##  error 
