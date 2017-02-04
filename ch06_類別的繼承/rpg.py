#! ecnoding:utf8

class Role:

    def __init__(self,name,level,blood):
        self.name = name
        self.level = level
        self.blood = blood

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


if __name__ =='__main__':
    swordsman = SwordsMan('Justin',1,200)
    print('SwordsMan',swordsman)
    magician = Magician('Monica',1,100)
    print('Magician',magician)
