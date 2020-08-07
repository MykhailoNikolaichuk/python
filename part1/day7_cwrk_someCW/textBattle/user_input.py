import fancy_modules as fancy
import form_table as tForm

def getNumberOfFighters():
    numberOfFighters = 0
    while True:
      try:
        numberOfFighters = int(input("how much of ya are gonna fight? \n"))
      except ValueError:
        fancy.slow_type("You wanna continue to foolin with me? gimme NUMBER!\n")
        continue
      else:
        break 
    return numberOfFighters

def confirmFighters(fightersList):
    while True:
        data = input("answer yes or y\n")
        if data.lower() not in ('yes', 'y'):
            fancy.slow_type("I don't get ur barking, let's pretend you want to mix stats\n")
            tForm.mixFighterStats(fightersList)
        else:
            fancy.slow_type("Alrighty then, Mr. {}\nLet's move on to fight arena\n".format(fancy.getLaughableName()))
            break

def welcomeScreen():
    while True:
        data = input("Please say hello to our leader\n")
        if data.lower() not in ('hi', 'hello'):
            fancy.slow_type("BE POLITE WITH PEOPLE AND THEY WILL BE POLITE WITH YOU\n")
        else:
            break


#add user name info