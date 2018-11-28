input_filepath = 'input.txt'

open_input = open(input_filepath, 'r')

content = open_input.readlines()

#print content #checking that i did get a line of strings

"""
First, I'd like to split these strings up into their three parts:
the name
the sector ID
the checksum

I can use split on the '-', but I'll have to find some way to ignore the dashes
within the name part (the alpha characters). Can split work backward?
"""

def histogram(L):
	histogram = {}
	for i in L:
		if i in histogram:
			histogram[i] += 1
		else:
			histogram[i] = 1
	return histogram



test_content = content[:3] #getting some content to work with

room_list = [] #i want this to be a list of lists with name, number, checksum

sectorsum = 0

#content = ['a-b-c-d-e-f-g-h-987[abcde]', 'aaaaa-bbb-z-y-x-123[abxyz]', 'not-a-real-room-404[oarel]', 'totally-real-room-200[decoy]']

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

#returns the histogram for the name string
for i in room_list:
	print 'line of', i
	checkchecksum = ''
	checksum = i[2]
	sector = i[1]
	print 'checksum of', checksum
	linehisto = histogram(i[0])
	print 'histogram follows', linehisto
	orderedlinehisto = [value[0] for value in sorted(linehisto.items(), key=lambda (key,value): (-value,key))]
	orderedlinehisto = orderedlinehisto[:5]
	print 'five most common', orderedlinehisto
	for i in orderedlinehisto:
		checkchecksum += i
	print 'as a string', checkchecksum
	if checkchecksum == checksum:
		sectorsum += int(sector)
	print 'total of sectors', sectorsum

print sectorsum