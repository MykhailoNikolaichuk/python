
# 1. Write a class named Animal that has
# 	a. a name
# 	b. an amount of energy and maximum_energy
# 	c. a method called Walk which removes 1 energy (down to 0)
# 	d. a method called Eat which adds 3 energy (up to the maximum)
# 2. Create an Animal that Walks until it runs out of energy, then Eats until full


class Animal:
    def __init__(self, name, energy, maximum_energy):
        self.name = name
        self.energy = energy
        self.maximum_energy = maximum_energy
    
    def walk(self):
        if self.energy > 0:
            self.energy = self.energy - 1
            print('Animal used 1 energy and walk a bit')
        
        if self.energy == 0:
            print('Animal to tired to walk')

    def eat(self):
        self.energy = self.energy + 3
        print('Animal restored 3 energy with eating')

        if self.energy >= self.maximum_energy:
            self.energy = self.maximum_energy
            print('Animal restored full health')

# animal_1 = Animal('Bobik', 10, 13)

# while animal_1.energy != 0:
#     animal_1.walk()

# while animal_1.energy != animal_1.maximum_energy:
#     animal_1.eat()

# 3. Create a Dog class that 
# 	a. inherits Animal
#	b. has a method called Play which removes 3 energy (down to 0)
# 	c. has a method called Pet which
# 		- asks the user for input
# 		- adds energy up to the maximum if the user says "good boy"
#		- adds no energy otherwise
# 4. Create a Dog that 
# 	- Plays until it runs of energy
# 	- asks for Pets
# 	- Eats until full if necessary

class Dog(Animal):
    def __init__(self, name, energy, maximum_energy):
        super().__init__(name, energy, maximum_energy)

    def play(self):
        if self.energy > 2:
            self.energy = self.energy - 3
            print('Animal used 3 energy and play a bit')
        
        if self.energy <= 0:
            print('Animal to tired to play')
            self.energy = 0

    def pet(self):
        user_input = input("Say something to your dog: ")
        if user_input == 'good boy':
            self.energy = self.maximum_energy
            print('restored full hp')
        else:
            print('you wont to pet ur doggo')

doggo_1 = Dog('Vovk', 15, 20)
while doggo_1.energy > 0:
    doggo_1.play()

doggo_1.pet()
while doggo_1.energy != doggo_1.maximum_energy:
    doggo_1.eat()

