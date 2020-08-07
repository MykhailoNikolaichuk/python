
# Write a function that
# 1. returns the Nth lowest number from a list
# 2. returns the lowest number if a second argument is not specified
# You can modify the function signature if needed
# Duplicates should only count once
def get_nth_lowest_number(number_list, nth = None):
	unique_list = list(set(number_list))
	unique_list.sort()
	if nth == None:
		return unique_list[0]
	else:
		return unique_list[nth - 1]
	pass

list_1 = [68, 60, 94, 42, 185, 95, 155]
list_2 = [120, 162, 83, 8, 198, 8, 176]
print(get_nth_lowest_number(list_1, 2))
print(get_nth_lowest_number(list_1, 5))
print(get_nth_lowest_number(list_1, 7))
print(get_nth_lowest_number(list_2, 1))
print(get_nth_lowest_number(list_2, 3))
print(get_nth_lowest_number(list_2, 5))