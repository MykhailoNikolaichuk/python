x = [13, 5, 6, 2, 5]
y = [5, 2, 5, 13]

def solution(x, y):
    return [i for i in x + y if i not in x or i not in y]
 







print(solution(x, y))
'''
# list = [x for x in range(50) if x % 3 == 0]
# print(list)
# solution(x, y)

merged = x + y
unique = list(set(merged))
# sol = [print(i) for i in unique]
print( )
print(int([6]))
# print(merged)
# print(unique)
# print(sol)
'''