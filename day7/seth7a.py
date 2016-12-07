input_filepath = 'input.txt'
input1 = open(input_filepath, 'r')
content_lines = input1.readlines()
content = [i.strip() for i in content_lines]

def inversion_checker(string): #a little function to test for inversions on strings
	for i in range (0,len(string) - 3):
		if string[i] + string[i + 1] == string[i + 3] + string[i + 2] and string[i] != string[i + 1]:
			return True

def string_checker(strings):
	tls_counter = 0
	for string in strings:
		even_inversions = 0
		odd_inversions = 0
		string = string.replace('[','*')
		string = string.replace(']','*')
		strings = string.split('*') #split up that row into strings
		for string_number in range(0,len(strings)): #for each one of these strings
			if string_number % 2 == 0: #for these strings that are even
				if inversion_checker(strings[string_number]) == True: #if they have an inversion
					even_inversions += 1
			if string_number % 2 != 0: #for those strings that are odd
				if inversion_checker(strings[string_number]) == True: #they have an inversion
					odd_inversions += 1
		if even_inversions > 0 and odd_inversions == 0:
			tls_counter += 1
			print 'tls count is', tls_counter, '\n'

print string_checker(content)