#dansolution18a

def newlineimport(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.replace("\n","")
	return input1

def addsafespaces(listing,endnumber):
	listing.insert(0,".")
	listing.insert(endnumber,".")
	return listing

def traptest(trapstring):
	if trapstring == "^^." or trapstring == ".^^" or trapstring == "^.." or trapstring == "..^":
		return "^"
	else:
		return "."

textimport = "inputtext.txt"
mining = newlineimport(textimport)
minearray = list(mining)
endlister = len(minearray) + 1
minefieldlength = 400000

#print minearray

minearray = addsafespaces(minearray,endlister)

minefield = [minearray]

for m in range(0,minefieldlength-1):
	newminerow = []
	for n in range(0,endlister-1):
		mineteststring = str(minefield[m][n]) + str(minefield[m][n+1]) + str(minefield[m][n+2])
		newminerow.append(traptest(mineteststring))
	newminerow = addsafespaces(newminerow,endlister)
	minefield.append(newminerow)

counter = 0

for m in range(0,minefieldlength):
	counter += minefield[m].count(".") - 2

print counter
