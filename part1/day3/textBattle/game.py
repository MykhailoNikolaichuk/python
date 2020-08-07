import text_art as tArt
import user_input as uInput
import fancy_modules as fancy


print(tArt.gamelogo)
fancy.slow_type("Say hello to yourself idiot!\nCall me Corporal Claw\n")

numberOfFighters = uInput.getNumberOfFighters()

fancy.slow_type("Hmm... You entered {} but there is {} of you\n".format(numberOfFighters, numberOfFighters + 1))
fancy.slow_type("Ah........\n", 25)
fancy.slow_type("Forget it, this one with keyboard and mouse participating only in internet fights, isn't you ?\n")

fancy.slow_type("Anyway, gimme the name of this 'Mr. {}'\n".format(fancy.getLaughableName()))
input()
# user_input here for f1 it probably will be for 1 element of array with fighter 0 one.

for x in range(1, numberOfFighters):
    fancy.slow_type("And how should I call this {} ? 'Mr. {}' or what?\n".format(fancy.getLaughableName(), fancy.getLaughableName()))
    input()
    # user input for rest of fighters


# when we got all names we check that user agree with prediction of corporal

# when all set, battle begin

# create rounds/ some images and stuff




























input("\n\nPress enter to exit ;)")