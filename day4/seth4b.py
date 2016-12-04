#advent of code, seth, 4b

input_filepath = 'input.txt'
input1 = open(input_filepath, 'r')
content = input1.readlines()

#now i'm going to make a searchable dictionary for the alphabet--i hope.

alphabet = 'abcdefghijklmnopqrstuvwxyz' #is this really the way to do this? hmm...

alphabet_index = []

for i in range(0,26):
	alphabet_index.append([alphabet[i],i])

alphabet_dict = dict(alphabet_index)

print alphabet_dict

#i think i also need a reverse dictionary?

alphabet_index2 = []

for i in range(0,26):
	alphabet_index2.append([i,alphabet[i]])

alphabet_dict_reverse = dict(alphabet_index2)

#print alphabet_dict_reverse

#now importing the room_line enginge from 4a

room_list = []

for i in content:
	#print 'line is', i #this is each line of content
	splitline = i.split('-')
	#print splitline #this gives me the line split into parts
	lineresults = [] #this is a blank string i'll now fill in
	reverse_checksum = ''
	checksum = ''
	sector = ''
	name = ''
	for i in splitline[-1]:
		if i.isalpha() == True:
			checksum = checksum + i
		if i.isdigit() == True:
			sector = sector + i
	for i in range(0,len(splitline) - 1):
		name = name + splitline[i]
	lineresults = [name, sector, checksum]
#	print 'lineresults are', lineresults #this is the string containing the name, ID, and checksum for each line
	room_list.append(lineresults) #adding the line results to the end result

#print room_list

#now onto the decrypting bit

cleartext = [] #this will be the deciphered text for each line

for i in room_list:
	#print i[1]
	cleartext_buffer = ''
	places = int(i[1]) % 26
	#print 'number of places ahead', places
	#print places
	for j in i[0]:
		#print j
		if j.isalpha() == True:
			position = 0 #i think this will let me search the dictionary?
			letter = j
#			print 'old letter is', letter
			if alphabet_dict[letter] + places < 26:
				position = alphabet_dict[letter] + places
			else:
				position = places - (26 - alphabet_dict[letter])
#			print 'new letter is', alphabet_dict_reverse[position]
			cleartext_buffer += alphabet_dict_reverse[position]
	cleartext.append([cleartext_buffer, i[1]])

for i in cleartext:
	if 'north' in i[0]:
		print i