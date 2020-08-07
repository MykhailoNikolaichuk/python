import re

text = """
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-z-]+\.(com|edu|net)')

matches = pattern.finditer(text)

# print(matches)

for match in matches:
    print(match)



num1 = 10_100_100
num2 = 10_100

print(num1 + num2)


def add(emp, emp_list=[]):
    emp_list.append(emp)
    print(emp_list)

add('misha')
add('vasya')