#adventday4a

import collections

input_file = 'day4input.txt'
roomcodes = []

def newlinefile(input_file1):
	input1 = open(input_file1, 'r')
	input1 = input1.read()
	input1 = input1.split("\n")
	return input1

def letterstringget(inputstring):
	for everyitem in range(0,len(inputstring)):
		if inputstring[everyitem].isdigit() == True:
			return inputstring[0:everyitem - 1].replace("-","")

def sectorcodeget(inputstring):
	firstdigit = 0
	sectorendID = 0
	digitcount = 0
	for everyitem in range(0,len(inputstring)):
		if inputstring[everyitem:(everyitem + 1)].isdigit() == True:
			if digitcount == 0:
				firstdigit = everyitem
				digitcount = 1
			else:
				sectorendID = everyitem
	return inputstring[firstdigit:sectorendID + 1]

def checksumget(inputstring):
	for everyitem in range(0,len(inputstring)):
		openbracket = inputstring.find("[")
		closedbracket = inputstring.find("]")
		return inputstring[openbracket + 1:closedbracket]

def checksumbuild(letterdictionary):	
	looper = max(letterdictionary.values())
	letterkeys = sorted(letterdictionary.keys())
	mychecksum = ""
	while looper > 0:
		for i in range(0,len(letterkeys)):
			if letterdictionary[letterkeys[i]] == looper:
				if len(mychecksum) < 5:
					mychecksum = str(mychecksum) + str(letterkeys[i])
		looper -= 1
	return mychecksum

def dictitembuild(inputstring):
	newdict = {}
	for i in range(0,len(inputstring)):
		if inputstring[i:i+1] not in newdict.values():
			newdict[inputstring[i:i+1]] = 0
	return newdict

def dictitemcount(inputstring,newdict):
	for i in range(0,len(inputstring)):
		if inputstring[i:i+1] in newdict:
			newdict[inputstring[i:i+1]] += 1 
	return newdict
			
roomcodes = newlinefile(input_file)
setlength = len(roomcodes) - 1

sectorsum = 0

for k in range(0,setlength):

	encryptedname = roomcodes[k]
	letterfreq1 = {}
	
	letterstring = letterstringget(roomcodes[k])
	sectorcode = int(sectorcodeget(roomcodes[k]))
	checksum = checksumget(roomcodes[k])
	letterfreq1 = dictitembuild(letterstring)
	letterfreq1 = dictitemcount(letterstring,letterfreq1)
	
	mychecksum1 = checksumbuild(letterfreq1)

	if mychecksum1 == checksum:
		sectorsum += sectorcode

	letterfreq1.clear()

print sectorsum
