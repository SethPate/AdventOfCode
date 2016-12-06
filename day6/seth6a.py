input_filepath = 'input.txt'

input1 = open(input_filepath, 'r')

content_lined = input1.readlines()

content = []

for i in content_lined: #this will get rid of the whitespace \n
	#print i
	i = i.strip()
	string = [i]
	content[len(content):] = string #cute equivalent to 'append'

columns_list = [] #a list of lists of the characters from each column

for i in range(0,len(content[0])): #this makes the list-of-lists long enough
	columns_list.append([])

for i in content: #this should add the characters to the right lists
	for j in range(0,len(i)):
		columns_list[j].extend(i[j])

plaintext = '' #this is the translated message (eventually)

for i in columns_list: #this sorts the strings by frequency and adds the most common to the plaintext
	histogram = {}
	for j in range(0,len(i)):
		histogram[i[j]] = i.count(i[j])
	histo_sorted = [value[0] for value in sorted(histogram.items(), key = lambda (key,value): (-value,key))]
	plaintext += histo_sorted[0]

print plaintext