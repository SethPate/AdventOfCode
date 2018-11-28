#dansolution9a

textimport = 'day9input.txt'

def newlineimport(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.replace("\n","")
	input1 = input1.replace(" ","")
	return input1

def numbergrab(a,b,c):
	return a[b+1:c]

def appender(a,b,c):
	return a[(int(b) + 1):(int(b) + 1 + int(c))]

def repeater(a,b):
	c = ""
	for i in range(0,int(b)):
		c = c + str(a)
	return c

explosivedata = newlineimport(textimport)
decompressedstring = ""
i = 0

while i < len(explosivedata):
	if explosivedata[i] != "(":
		decompressedstring = decompressedstring + str(explosivedata[i])
		i += 1
	elif explosivedata[i] == "(":
		j = explosivedata.find("x",i)
		k = explosivedata.find(")",i)
		repeatlen = numbergrab(explosivedata,i,j)
		repeatfreq = numbergrab(explosivedata,j,k)
		decompressedstring = decompressedstring + repeater(appender(explosivedata,k,repeatlen),repeatfreq)
		i = int(k) + 1 + int(repeatlen)
		
print len(decompressedstring)
