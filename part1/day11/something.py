randomlist = [1, 0, 53, -3, 13, 30, 77]

def find_second_max(list):
    fmax = list[0]
    smax = list[0]
    for item in list:
        if item > fmax:
            smax = fmax
            fmax = item
        elif (item < fmax and item > smax):
            smax = item
    
    return smax

print(find_second_max(randomlist))