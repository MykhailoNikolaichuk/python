class Employee:
    motto = 'Code Fast and Code Clean'
    def __init__(self, name, surname, pay):
        self.name = name
        self.surname = surname
        self.pay = pay
    def introduce(self):
        print(f'I\'m {self.name} {self.surname} with pay = {self.pay}')
        pass
    
    @classmethod
    def change_moto(cls, motto):
        cls.motto = motto
    
    @staticmethod
    def agree_on_pidor(name):
        if(name == 'Igor'):
            return 'Agree, Mr. Salad pidorasina'
        else:
            return 'Norm, chelik'


vasya = Employee('Vasya', 'Pober', 1000000)

print(vasya.motto)
Employee.change_moto('huy sasi guboy tryasi')
print(Employee.agree_on_pidor('Igor'))