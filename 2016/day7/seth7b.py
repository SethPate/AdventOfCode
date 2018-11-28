input_filepath = 'input.txt'
input1 = open(input_filepath, 'r')
content_lines = input1.readlines()
content = [i.strip() for i in content_lines]

ssl_count = 0 #this is the goal counter

def inversion_checker(string):
	inversion_list = []
	string = string.replace('[','*')
	string = string.replace(']','*')
	string = string.split('*')
	for i in string[0::2]: #checks only the even strings
		for j in range(0,len(i) - 2): #checks every character in that string
			if i[j] == i[j + 2] and i[j] != i[j+1]: #finds aba triplets
				inversion_list.append(str(i[j+1] + i[j] + i[j+1])) #appends triplets to the list, but INVERTS them
	for i in string[1::2]: #checks the odd strings
		for j in range(0,len(inversion_list)): #checks every inversion in the list
			if inversion_list[j] in i:
				return True

for i in content:
	if inversion_checker(i) == True:
		ssl_count += 1

print ssl_count