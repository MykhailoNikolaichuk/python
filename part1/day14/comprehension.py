
# nums = [n for n in range(10)]

# print(nums)

# my_list = [n for n in nums]
# print(my_list)

# my_list = [n * n  for n in nums]
# print(my_list)

# my_list = [n * n  for n in nums if n % 2 == 0]
# print(my_list)

# letters = 'abcd'
# numbers = '0123'

# my_list = [(letter, number) for letter in letters for number in numbers]
# print(my_list)


names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {name: hero for name, hero in zip(names, heroes)}
print(my_dict)