#dansolution7a

textimport = 'day7input.txt'

def newlinefile(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.split("\n")
	return input1

def outsideofbrackets(a,c):
	if c == 0:
		if a[0:1] == a[3:4]:
			if a[1:2] == a[2:3] and a[1:2] != a[0:1]:
				abba = 1
			else:
				abba = 0
		else:
			abba = 0
	else:
		abba = 1
	return abba
	
def insideofbrackets(a,c):
	if c == 1:
		if a[0:1] == a[3:4]:
			if a[1:2] == a[2:3] and a[0:1] != a[1:2]:
				abba = 0
			else:
				abba = 1
		else:
			abba = 1
	else:
		abba = 0
	return abba

def bracketswitch(a):
	if a == "[":
		return "on"
	else:
		return "off"
	
	if a == "]":
		return "off"
	else:
		return "on"

ipaddresses = newlinefile(textimport)
counter = 0

finaltotal = 0
k = 2
stringtest = ""
for k in range(0,len(ipaddresses)-1):
	for j in range(0,len(ipaddresses[k])-3):
		switch = "off"
		outsidescore = 0
		insidescore = 1
		for j in range(0,len(ipaddresses[k])-3):
			stringtest = ipaddresses[k][j:j+4]
			if stringtest.find("[") == 0 or stringtest.find("]") == 0:
				switch = bracketswitch(stringtest[0:1])

			elif stringtest.find("[") > 0 or stringtest.find("]") > 0:
				switch = switch
			
			else:
				if switch == "off":
					outsidescore = outsideofbrackets(stringtest,int(outsidescore))
				else:
					insidescore = insideofbrackets(stringtest,int(insidescore))
	if outsidescore + insidescore == 2:
		counter += 1

print counter
