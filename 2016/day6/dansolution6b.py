#dansolution6a

textimport = 'day6input.txt'

def newlinefile(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.split("\n")
	return input1

def dictitembuild(a):
	newdict = {}
	for i in range(0,len(a)):
		if a[i][0:1] not in newdict.values():
			newdict[a[i:i+1]] = 0
	return newdict

def dictitemcount(a,newdict):
	for i in range(0,len(a)):
		if a[i][0:1] in newdict:
			newdict[a[i:i+1]] += 1 
	return newdict

def charposstring(a,b):
	newstring = ""
	for i in range(0,len(a)):
		newstring = newstring + str(a[i][b:b+1])
	return newstring

def commonletter(a):
	avalues = a.values()
	akeys = a.keys()
	j = min(avalues)
	for i in range(0,len(avalues)):
		if avalues[i] == j:
			x = i
	return akeys[x]

textimport = newlinefile(textimport)
finalanswer = ""

for x in range(0,len(textimport[0])):
	columnstring = charposstring(textimport,x)
	letterfreq = dictitembuild(columnstring)
	letterfreq = dictitemcount(columnstring,letterfreq)
	finalanswer = finalanswer + commonletter(letterfreq)

print finalanswer
