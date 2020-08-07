def get_nth_lowest_number(number_list, nth=0):
  number_list = list(set(number_list)) #to remove duplicates
  number_list.sort()
  if nth > len(number_list) - 1:
    nth = len(number_list) - 1
  return(number_list[nth])

list_1 = [68, 60, 94, 42, 185, 95, 155]
list_2 = [120, 162, 83, 8, 198, 8, 176]
print(get_nth_lowest_number(list_1, 2))
print(get_nth_lowest_number(list_1, 5))
print(get_nth_lowest_number(list_1, 7))
print(get_nth_lowest_number(list_2, 1))
print(get_nth_lowest_number(list_2, 3))
print(get_nth_lowest_number(list_2, 5))