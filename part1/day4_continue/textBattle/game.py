import os
import text_art as tArt
from fighter import Fighter
import user_input as uInput
import fancy_modules as fancy
import form_table as tForm
from prettytable import PrettyTable

input()
# '''
print(tArt.gamergirl)
fancy.slow_type("Ahoy, matey!\nYou must be searching for Fight Arena?\nOh of course you are, but first you need to show your manners\n")
uInput.welcomeScreen()
os.system("cls")

print(tArt.gamelogo)
fancy.sleepSomeTime(1)
fancy.slow_type("Say hello to yourself idiot!\nCall me Corporal Claw\n")

numberOfFighters = uInput.getNumberOfFighters()

fancy.slow_type("Hmm... You entered {} but there are {} of you\n".format(numberOfFighters, numberOfFighters + 1))
fancy.slow_type("Ah........\n", 25)
fancy.slow_type("Forget it, this one with keyboard and mouse participating only in internet fights, aren't you ?\n")


fightersList = []
# fancy.slow_type(input("Anyway, gimme the name of this 'Mr. {}'\n".format(fancy.getLaughableName())))
fancy.slow_type("Anyway, gimme the name of this 'Mr. {}'\n".format(fancy.getLaughableName()), 250)
fightersList.append(Fighter(input('')))
tForm.fillFighterWithRandom(fightersList[len(fightersList) - 1])
# user_input here for f1 it probably will be for 1 element of array with fighter 0 one.

for x in range(1, numberOfFighters):
    fancy.slow_type("And how should I call this {} ? 'Mr. {}' or what?\n".format(fancy.getLaughableName(), fancy.getLaughableName()), 250)
    fightersList.append(Fighter(input('')))
    tForm.fillFighterWithRandom(fightersList[len(fightersList) - 1])
    # user input for rest of fighters

fancy.slow_type("You know, I'm the one of this guys who can predict things...\n", 100)
fancy.slow_type("YOU GONNA DIE\n", 10)
fancy.sleepSomeTime(0.5)
print("*cough*")
fancy.sleepSomeTime(1.5)
fancy.slow_type("Jokes aside, I weigh your squad roughly:\n", 100)
tForm.printTable(fightersList)
fancy.slow_type("tell me is this fight table seems right to you?\n", 100)
uInput.confirmFighters(fightersList)

fancy.sleepSomeTime(1.0)
for round in range(1, 15):
    if len(fightersList) == 0: 
        print('Unlucky but everyone died, there is no winner in this game')
        break
    elif len(fightersList) == 1: 
        print('And we have the WINNER, and we got the name here - {}'.format(fightersList[0].name.upper()))
        break
    else: 
        tForm.fightOneRound(fightersList, round)
        tForm.printTable(fightersList)
        fancy.sleepSomeTime(3.0)
else:
    print('Absolute MADNESS those players managed to survive 15 roundes')


# '''


#user input at start and insult

#gamergirld welcome

#clear screen
#import os
#os.system("cls")


# fightersList = []

# fightersList.append(Fighter('Luke'))
# tForm.fillFighterWithRandom(fightersList[len(fightersList) - 1])
# fightersList.append(Fighter('Sky'))
# tForm.fillFighterWithRandom(fightersList[len(fightersList) - 1])
# fightersList.append(Fighter('Walter'))
# tForm.fillFighterWithRandom(fightersList[len(fightersList) - 1])

# tForm.printTable(fightersList)

# fightersList[0].damageNext(fightersList[1])
# del fightersList[0]


        # print(fightersList[x].name)
        # print(len(fightersList))
# tForm.fightOneRound(fightersList)

input("\n\nPress enter to exit ;)")