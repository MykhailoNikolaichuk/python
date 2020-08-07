fruits = {
    1: 'kiwi', 
    2: 'pear', 
    3: 'kiwi', 
    4: 'banana', 
    5: 'melon', 
    6: 'banana', 
    7: 'melon', 
    8: 'pineapple', 
    9: 'apple', 
    10: 'pineapple', 
    11: 'cucumber', 
    12: 'pineapple', 
    13: 'cucumber', 
    14: 'orange', 
    15: 'grape', 
    16: 'orange', 
    17: 'grape', 
    18: 'apple', 
    19: 'grape', 
    20: 'cherry', 
    21: 'pear', 
    22: 'cherry', 
    23: 'pear', 
    24: 'kiwi', 
    25: 'banana', 
    26: 'kiwi', 
    27: 'apple', 
    28: 'melon', 
    29: 'banana', 
    30: 'melon', 
    31: 'pineapple', 
    32: 'melon', 
    33: 'pineapple', 
    34: 'cucumber', 
    35: 'orange', 
    36: 'apple', 
    37: 'orange', 
    38: 'grape', 
    39: 'orange', 
    40: 'grape', 
    41: 'cherry', 
    42: 'pear', 
    43: 'cherry', 
    44: 'pear', 
    45: 'apple', 
    46: 'pear', 
    47: 'kiwi', 
    48: 'banana', 
    49: 'kiwi', 
    50: 'banana', 
    51: 'melon', 
    52: 'pineapple', 
    53: 'melon', 
    54: 'apple', 
    55: 'cucumber', 
    56: 'pineapple', 
    57: 'cucumber', 
    58: 'orange', 
    59: 'cucumber', 
    60: 'orange', 
    61: 'grape', 
    62: 'cherry', 
    63: 'apple', 
    64: 'cherry', 
    65: 'pear', 
    66: 'cherry', 
    67: 'pear', 
    68: 'kiwi', 
    69: 'pear', 
    70: 'kiwi', 
    71: 'banana', 
    72: 'apple', 
    73: 'banana', 
    74: 'melon', 
    75: 'pineapple', 
    76: 'melon', 
    77: 'pineapple', 
    78: 'cucumber', 
    79: 'pineapple', 
    80: 'cucumber', 
    81: 'apple', 
    82: 'grape', 
    83: 'orange', 
    84: 'grape', 
    85: 'cherry', 
    86: 'grape', 
    87: 'cherry', 
    88: 'pear', 
    89: 'cherry', 
    90: 'apple', 
    91: 'kiwi', 
    92: 'banana', 
    93: 'kiwi', 
    94: 'banana', 
    95: 'melon', 
    96: 'banana', 
    97: 'melon', 
    98: 'pineapple', 
    99: 'apple', 
    100: 'pineapple', 
}


def subtract_sum(number):
    def sum_digits(n):
        s = 0
        while n:
            s += n % 10
            n //= 10
        return s

    my_number = number - sum_digits(number)

    while True:
        if my_number < 1 or my_number > 100:
            my_number = my_number - sum_digits(my_number)
            print(my_number)
        else:
            break

    return fruits.get(my_number)

print(subtract_sum(10))

"""
def subtract_sum(n):
  n -= (sum([int(i) for i in str(n)]))
  while not n in fruit:
    n -= (sum([int(i) for i in str(n)]))
  return fruit[n]



def subtract_sum(number):
    codes = {
        "kiwi": [1, 3, 24, 26, 47, 49, 68, 70, 91, 93],
        "pear": [2, 21, 23, 42, 44, 46, 65, 67, 69, 88],
        "banana": [4, 6, 25, 29, 48, 50, 71, 73, 92, 94, 96],
        "melon": [5, 7, 28, 30, 32, 51, 53, 74, 76, 95, 97],
        "pineapple": [8, 10, 12, 31, 33, 52, 56, 75, 77, 79, 98, 100],
        "apple": [9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99],
        "cucumber": [11, 13, 34, 55, 57, 59, 78, 80],
        "grape": [15, 17, 19, 38, 40, 61, 82, 84, 86],
        "orange": [14, 16, 35, 37, 39, 58, 60, 83],
        "cherry": [20, 22, 41, 43, 62, 64, 66, 85, 87, 89],
    }
    while number > 0:
        number -= sum(int(n) for n in list(str(number)))
        for k, v in codes.items():
            if number in v:
                return k
  """