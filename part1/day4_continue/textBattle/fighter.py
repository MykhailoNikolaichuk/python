import random

class Fighter:
  def __init__(self, name):
    self.name = name
    self.health = 1
    self.damage = 1
    self.defense = 1
  def damageNext(self, enemy):
    damage = self.damage + random.randint(-10, 10) - enemy.defense
    enemy.health = enemy.health - damage
    if enemy.health < 0: print('{} killed {} with {} damage punch'.format(self.name, enemy.name, damage))
    else: print('{} {} {} with {} damage hit'.format(self.name,random.choice(['punched','striked','kicked','shocked','smited','bited','stabbed','smacked']), enemy.name, damage))