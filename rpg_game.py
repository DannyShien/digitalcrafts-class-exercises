#RPG GAME 1
class Character: 
  def __init__(self, health, power):
    self.health = health
    self.power = power

  def status(self):
   if self.health > 0: 
      return True
   return False

  def print_status(self):
    print('You have %d health and %d power.' % (self.health, self.power))

class Hero(Character):
  def __init__(self, health, power):
    self.name = 'Heo'

  def attack(self, enemy):
    enemy.health -= self.power
    print('You do %d damamge to the Goblin.' % self.power)

  def print_status(self):
    print('You have %d health and %d power.' % (self.health, self.power))

class Goblin(Character):
  def __init__(self, health, power):
    self.name = 'Golin'

  def attack(self, swordsman):
    swordsman.health -= self.power
    print('The Goblin does %d damage to you.' % self.power)

  def print_status(self): 
    print('You have %d health and %d power.' % (self.health, self.power))

class zombie(Character):
  def __init__(self, health, power):
    self.name = 'Walker'

  def attack(self, dead):
    #if swordsman.health > 6:
    if self.health > 6:
      #swordsman.health -= self.power
      self.health-= self.power
    print('The Zombie')

  def status(self):
    #if self.health > 0: 
      return True


  def print_status(self):
    print('You have %d health and %d power.' % (self.health, self.power))


# def begin():
#   swordsman = Hero(10, 5)
#   enemy = Goblin(6, 2)
#   dead = Walker(8, 5)

#   while enemy.status() and swordsman.status():
#     def print_status(self):
#       def print_status(self):
#       break
#         print()