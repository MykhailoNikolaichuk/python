"""
If we have an array [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive 
but 6 is not, so that's the first non-consecutive number.
"""

def first_non_consecutive(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            break
        if arr[i] + 1 != arr[i + 1]:
            return arr[i + 1]
    else:
        return None



print(first_non_consecutive([1, 2, 3, 4, 5, 6, 8]))

"""
def first_non_consecutive(arr):
    if not arr: return 0
    for i, x in enumerate(arr[:-1]):
        if x + 1 != arr[i + 1]:
            return arr[i + 1]




            def first_non_consecutive(a):
    i = a[0]
    for e in a:
        if e != i:
            return e
        i += 1
    return None


    def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            return arr[i]

"""