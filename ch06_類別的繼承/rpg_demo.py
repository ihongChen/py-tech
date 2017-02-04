#encoding : utf8

import rpg

def draw_fight(role):
    print(role,end=' ')
    role.fight()

swordsman = rpg.SwordsMan('Justin',1,200)
draw_fight(swordsman)

class Duck:
    pass

duck = Duck()
duck.fight = lambda :print('呱呱')
draw_fight(duck) # <__main__.Duck object at 0x.....> 呱呱
