#dansolution7b

textimport = 'day7input.txt'

def newlinefile(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.split("\n")
	return input1

def bracketswitch(a):
	if a == "[":
		return "on"
	else:
		return "off"
	
	if a == "]":
		return "off"
	else:
		return "on"

def abastring(a):
	if a[0:1] == a[2:3] and a[0:1] != a[1:2]:
		return a[0:3]
	else:
		return 0

def abaflipper(a):
	return a[1:2] + a[0:1] + a[1:2]

ipaddresses = newlinefile(textimport)
counter = 0

finaltotal = 0
stringtest = ""

for k in range(0,len(ipaddresses)-1):
	match = 0
	BABstrings = []
	switch = "off"
	for j in range(0,len(ipaddresses[k])-2):
		stringtest = ipaddresses[k][j:j+3]
		#print stringtest
		if stringtest.find("[") == 0 or stringtest.find("]") == 0:
			switch = bracketswitch(stringtest[0:1])

		elif stringtest.find("[") > 0 or stringtest.find("]") > 0:
			switch = switch
			
		else:
			if switch == "off" and abastring(stringtest) != 0:
				BABstrings.append(abaflipper(stringtest))
	switch = "off"
	for j in range(0,len(ipaddresses[k])-2):
		
		stringtest = ipaddresses[k][j:j+3]
		if stringtest.find("[") == 0 or stringtest.find("]") == 0:
			switch = bracketswitch(stringtest[0:1])
		elif stringtest.find("[") > 0 or stringtest.find("]") > 0:
			switch = switch
		else: 
			if switch == "on" and stringtest in BABstrings:
				match = 1

	counter += match

print counter
