

# Write a function that
# 1. returns "even" for integers divisible by 2
# 2. returns "odd" for integers not divisible by 2
# 3. returns "not how it works" for numbers that are not integers
# 4. returns "not a number" for other inputs
def get_type_of_number(number):
	if type(number) == int:
		if number % 2 == 0:
			return "even"
		return "odd"
	elif type(number) == float:
		return "not how it works"
	else:
		return "not a number"
	pass

print(get_type_of_number(35))
print(get_type_of_number(12))
print(get_type_of_number(-51))
print(get_type_of_number(42.5))
print(get_type_of_number(64))
print(get_type_of_number(5 * 0.33))
print(get_type_of_number("a dog"))