
# Write a function that
# 1. receives a list of numbers
# 2. prints their sum
# 3. throws an exception if it receives anything other than a list of numbers
def add_numbers(number_list):
	if type(number_list) != list:
		raise Exception
	for item in number_list:
		if type(item) is not int:
			raise TypeError
	
	print(sum(number for number in number_list))
	
	pass

add_numbers([5, 3, 7])

try:
	add_numbers(["foo", "bar", 5])
except Exception as e:
	print("Did not receive the right arguments: " + e)

try:
	add_numbers(5)
except Exception as e:
	print("Did not receive the right arguments: " + e)

try:
	add_numbers({ "five" : 5, "three" : 3, "seven" : 7})
except Exception as e:
	print("Did not receive the right arguments: " + e)