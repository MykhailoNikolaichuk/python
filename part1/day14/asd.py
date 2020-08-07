# test.assert_equals(quadratic(0,1), (1, -1, 0))
# test.assert_equals(quadratic(4,9), (1, -13, 36))
# test.assert_equals(quadratic(2,6), (1, -8, 12))
# test.assert_equals(quadratic(-5,-4), (1, 9, 20))

def quadratic(x1, x2):
    x = 1
    first = x * x
    second = (-x) * x2 - x1 * x
    third = x1 * x2
    return (first, second, third)

print(quadratic(4,9))