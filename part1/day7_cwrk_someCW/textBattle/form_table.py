import random
import text_art as tArt
from fighter import Fighter
import fancy_modules as fancy
from prettytable import PrettyTable
from pprint import pprint

fightTable = PrettyTable()
fightTable.field_names = ["Fighter name", "Damage", "Health", "Defense"]

def addRowWithFighter(fighter):
  fightTable.add_row([fighter.name, fighter.damage, fighter.health, fighter.defense])

def fillFighterWithRandom(fighter):
  fighter.damage = random.randint(50, 100)
  fighter.health = random.randint(200, 400)
  fighter.defense = random.randint(10, 30)

def printTable(fightersList):
    fightTable.clear_rows()
    for x in range(len(fightersList)):
        addRowWithFighter(fightersList[x]) 
    print(fightTable)

def mixFighterStats(fightersList):
    fightTable.clear_rows()
    for x in range(len(fightersList)):
        fillFighterWithRandom(fightersList[x])
        addRowWithFighter(fightersList[x])
    print(fightTable)

def fightOneRound(fightersList, number = 666):
    print('\n{} ROUND {} {}\n'.format(tArt.swordleft, number, tArt.swordright))
    fancy.sleepSomeTime(1.0)
    for x in range(0, len(fightersList)):
        if x == len(fightersList) - 1: thisOneWillGetHit = fightersList[0]
        else: thisOneWillGetHit = fightersList[x + 1]
        fightersList[x].damageNext(thisOneWillGetHit)
        
        if thisOneWillGetHit.health <= 0:
            print('\n{} What a death of {} also known as Mr. {} {}\n'.format(tArt.death, thisOneWillGetHit.name, fancy.getLaughableName(), tArt.death))
            for x in range(0, len(fightersList)):
                if fightersList[x].health <= 0: 
                    del fightersList[x]
                    break
            break
        fancy.sleepSomeTime(0.5)
    


# fightersList = []

# fightersList.append(Fighter('Luke'))
# fillFighterWithRandom(fightersList[len(fightersList) - 1])
# fightersList.append(Fighter('Sky'))
# fillFighterWithRandom(fightersList[len(fightersList) - 1])
# fightersList.append(Fighter('Walter'))
# fillFighterWithRandom(fightersList[len(fightersList) - 1])

# fighter1 = Fighter()
# fighter1.name = 'Tolik'
# fillFighterWithRandom(fighter1)


