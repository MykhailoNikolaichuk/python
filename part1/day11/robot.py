class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
    
    def introduce_self(self):
        print(f'Hi, my name is {self.name}, I\'m {self.color} color and I weight {self.weight} pounds')
