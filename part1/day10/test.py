
def total(initial =5, *num, **key):
    print(f'initian = {initial}\nnum = {num}\nkey = {key}')
    count = initial
    for n in num:
        count+=n
    for k in key:
        count+=key[k]
    return count
# print(total(100,2,3,5, clouds=50, stars=100, zalupa=20))



def f(x = 100, y = 100): 
   return(x+y, x-y) 
x, y = f(y = 200, x = 100) 
# print(x, y) 

# print(eval('1 + 3 * 2'))

def bread(func):
    def filler():
        print('<----->')
        func()
        print('<----->')
    return filler

def salad(func):
    def filler():
        print('-salad-')
        func()
        print('-salad-')
    return filler


@bread
@salad
def sausage():
    print(' (((O ')

# sausage()


randomLine = 'Hello guys u menya vse ne nais'
# print( r'\n')


for number in range(1, 100):
    for i in range(2, number):
        if(number % i) == 0:
            break
    else:
        print(number)


list1, list2 = [123, 'xyz'], [456, 'abc']
print(list1, list2)
print(list2, list1)























