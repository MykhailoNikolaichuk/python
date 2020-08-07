# def expression_matter(a, b, c):
#     max = 1
#     if a + b + c > max: max = a + b + c
#     if a + b * c > max: max = a + b * c
#     if a * b + c > max: max = a * b + c
#     if a * b * c > max: max = a * b * c
#     if a * (b + c) > max: max = a * (b + c)
#     if (a + b) * c > max: max = (a + b) * c
#     return max


def expression_matter(a, b, c):
    return max(
        a+b+c,
        a+b*c,
        (a+b)*c,
        a*b+c,
        a*(b+c),
        a*b*c
        )

print(expression_matter(1, 2 , 3))