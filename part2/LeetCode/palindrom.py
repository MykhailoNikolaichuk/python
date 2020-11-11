potential_palindromme = 'abc'
potential_palindromme2 = 'abcba'

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome(potential_palindromme))
print(is_palindrome(potential_palindromme2))