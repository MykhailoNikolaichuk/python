# 1. Write a class named Animal that has
# 	a. a name
# 	b. an amount of energy and maximum_energy
# 	c. a method called Walk which removes 1 energy (down to 0)
# 	d. a method called Eat which adds 3 energy (up to the maximum)
class Animal:
    
    def __init__(self, name, energy, maximum_energy):
        self.name = name
        self.energy = energy
        self.maximum_energy = maximum_energy

    def walk(self):
        if self.energy <= 0:
            print('Animal tired and cannot walk anymore')
        else:
            print('Animal walked a bit and used 1 energy')
            self.energy = self.energy - 1

    
    def eat(self):
        self.energy = self.energy + 3
        print('Animal eating...')
        if self.energy > self.maximum_energy:
            self.energy = self.maximum_energy
            print('Animal has full energy now')
    
# 2. Create an Animal that Walks until it runs out of energy, then Eats until full

# animal_1 = Animal('Kesha', 8, 10)
# while animal_1.energy != 0:
#     animal_1.walk()

# animal_1.walk()

# while animal_1.energy != animal_1.maximum_energy:
#     animal_1.eat()

# 3. Create a Dog class that 
# 	a. inherits Animal
#	b. has a method called Play which removes 3 energy (down to 0)
# 	c. has a method called Pet which
# 		- asks the user for input
# 		- adds energy up to the maximum if the user says "good boy"
#		- adds no energy otherwise

class Dog(Animal):
    
    def __init__(self, name, energy, maximum_energy):
        super().__init__(name, energy, maximum_energy)

    def play(self):
        if self.energy <= 0:
            print(f'{self.name} tired and cannot play anymore')
        else:
            print(f'{self.name} played a bit and used 3 energy')
            self.energy = self.energy - 3
            if self.energy < 0:
                self.energy = 0

    def pet(self):
        user_input = input("Say something to your dog: ")
        if user_input == 'good boy':
            self.energy = self.maximum_energy
            print(f'{self.name} got admired by your speech and have full energy now')
    
# 4. Create a Dog that 
# 	- Plays until it runs of energy
# 	- asks for Pets
# 	- Eats until full if necessary

dog_1 = Dog('Bobik', 15, 20)

while dog_1.energy != 0:
    dog_1.play()

dog_1.play()

dog_1.pet()

while dog_1.energy != dog_1.maximum_energy:
    dog_1.eat()
