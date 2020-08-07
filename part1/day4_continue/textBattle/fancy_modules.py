import sys,time,random

def slow_type(t, typing_speed = 75): #TODO: change it to 75
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

def sleepSomeTime(timeToSleep):
    time.sleep(timeToSleep)

def getLaughableName():
    names = ['Amateur','A-hole','Banana','Beefy','Bing Bong','Buffoon','Bumblebee','Burrito','Butterfingers','Cheeks','Cheesy','Cheeseball','Chewbacca','Chipmunk','Chipmunk Cheeks','Chippy','Chubs','Chunkamunk','Class Clown','Clown','Clumsy Wumsy','Comedian','Comedy Central','Comic','Cookie','Crazy','Doink','Donkey','Doofy','Duckie','Dumbo','Energizer Bunny','Giggles','Goofball','Goofy','Fatty','Fish Face','Funny man','Fuzzy Wuzzy','Hater','Haterade','Hefty Wefty','Jabba','Jazzy','Joker','Jokes','Jokester','Kooky','Madcap','Mando','McLovin','Meatball','Noob','Noodles','Nut','Nutty','Pork Chop','Punk','Rook','Rookie','Q-Tip','Rico Suave','Screech','Screwball','Seinfeld','Silly Goof','Spock','Spaghetti','Squints','Squirrel','Squirt','Stinker','String bean','Tater','Tater Tot','Tiny','Tootsie Pop','Urkel']
    return random.choice(names)
    
# def getRandomAttackName():
    # names = ['punched','strikes','kicked','shocked','smited','beated','stabbed','smacked']
    # return 