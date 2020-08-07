import random
from fighter import Fighter
from prettytable import PrettyTable
from pprint import pprint

def addRowWithFighter(fighter):
  fightTable.add_row([fighter.name, fighter.damage, fighter.health, fighter.defense])

def fillFighterWithRandom(fighter):
  fighter.damage = random.randint(50, 100)
  fighter.health = random.randint(200, 400)
  fighter.defense = random.randint(10, 30)

fightersList = []

fightersList.append(Fighter('Luke'))
fillFighterWithRandom(fightersList[len(fightersList) - 1])
fightersList.append(Fighter('Sky'))
fillFighterWithRandom(fightersList[len(fightersList) - 1])
fightersList.append(Fighter('Walter'))
fillFighterWithRandom(fightersList[len(fightersList) - 1])




# fighter1 = Fighter()
# fighter1.name = 'Tolik'
# fillFighterWithRandom(fighter1)
    
fightTable = PrettyTable()
fightTable.field_names = ["Fighter name", "Damage", "Health", "Defense"]
for x in range(len(fightersList)):
    addRowWithFighter(fightersList[x])
    
print(fightTable)



