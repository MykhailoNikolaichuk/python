import re
# Write a function that
# 1. counts each occurence of a letter in a string
# 2. returns a dictionary in the form of { "a" : 3, "c" : 5 } etc
# 3. calculates and prints the most used letter in the dictionary
# The function should be case-insensitive and ignore other characters
def count_letters(text):
	nlist = re.findall(r'[a-z]', text.lower())
	ndict = dict((x, nlist.count(x)) for x in set(nlist))

	print(f'Most used letter is - {max(ndict, key=ndict.get)}')
	return ndict

print(count_letters("Mea navis aericumbens anguillis abundant."))
