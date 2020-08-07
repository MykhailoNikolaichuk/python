import fancy_modules as fancy

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
