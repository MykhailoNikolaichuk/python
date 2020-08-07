import re
# Write a function that
# 1. collects all the numbers from 04_files_sample.txt
# 2. prints each number on a line in a new file named 04_output_files.txt
def extract_numbers(file, output):
	with open(file, 'r') as f:
		file_content = f.read()

	numbers = re.findall(r'\d+', file_content)
	
	with open(output, 'w') as f:
		for number in numbers:
			f.write(number + '\n')

extract_numbers("04_sample_files.txt", "04_output_files.txt")