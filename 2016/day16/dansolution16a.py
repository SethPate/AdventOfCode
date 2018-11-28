#dansolution16a

puzzleinput = "11110010111001001"

def dragoncurve(stringinput,discsize):
	newstring = stringinput
	while len(newstring) < discsize:
		a = newstring
		b = a[::-1]
		d = ""
		for c in range(0,len(b)):
			if b[c] == '0':
				d = d + str(1)
			else:
				d = d + str(0)
		newstring = str(a) + "0" + str(d)
	return newstring[0:discsize]

def checksummer(stringinput):
	d = ""
	c = 0
	while c < len(stringinput):
		if stringinput[c:c+1] == stringinput[c+1:c+2]:
			d = d + str(1)
		else:
			d = d + str(0)
		c += 2
	return d

def checksumcomplete(stringinput):
	if len(stringinput) % 2 == 1:
		return "DONE"
	else:
		return "NOPE"

checksum = ""
stringer = dragoncurve(puzzleinput,35651584)
checksumholder = checksummer(stringer)

while checksumcomplete(checksumholder) != "DONE":
	checksum = checksummer(checksumholder)
	checksumholder = checksum
	
print checksumholder
