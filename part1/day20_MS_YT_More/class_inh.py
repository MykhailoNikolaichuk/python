class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f'{first.lower()}.{last.lower()}@gameloft.com'
        self.pay = pay

    def full_info(self):
        print(f'name = {self.first} {self.last} with {self.email}')

    @classmethod
    def change_raise_amt(cls, amount):
        cls.raise_amt = amount
    
    @staticmethod
    def make_announcement(phrase):
        print(f'{phrase.upper()} !!!')


class Developer(Employee):
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang



class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # def __str__(self):
    #     return f'class instance of {self.email}'

    def __repr__(self):
        return f'class representation of {self.email}'


bogdan = Employee('Bogdan', 'Racovita', 1000)
andrey = Developer('Andrey', 'Cigoran', 500, 'python')

manager_1 = Manager('Jeff', 'Bezos', 99999)
# print(manager_1.__dict__)
# manager_1.add_employee(bogdan)
# manager_1.add_employee(andrey)
# print(manager_1.__dict__)
# manager_1.remove_employee(bogdan)
# print(manager_1.__dict__)
    
print(manager_1)
