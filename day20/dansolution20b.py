#dansolution20b

#my 20a wouldn't work at all. going with a wholly-different approach.
#this should solve a and b.

textinput = "day20input.txt"

def newlineimport(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.split("\n")
	return input1

blockranges = newlineimport(textinput)
blocklist = []

for n in range(0,len(blockranges)-1):
	blockholder = blockranges[n]
	combomin = int(blockholder[0:blockholder.find("-",0)])
	combomax = int(blockholder[blockholder.find("-",0) + 1:])
	blocklist.append((combomin, combomax))

blocklist.sort(key=lambda tup: tup[0])

consolidatedblocklist = []
currentmin = blocklist[0][0]
currentmax = blocklist[0][1]
consolidatedblocklist.append([blocklist[0][0],blocklist[0][1]])
j = 0

for n in range(1,len(blocklist)):	
	if blocklist[n][0] <= consolidatedblocklist[j][1] + 1 and blocklist[n][1] >= consolidatedblocklist[j][1] + 1:
		consolidatedblocklist[j][1] = blocklist[n][1]
	elif blocklist[n][0] > consolidatedblocklist[j][1] + 1 and blocklist[n][1] > consolidatedblocklist[j][1] + 1:
		consolidatedblocklist.append([blocklist[n][0],blocklist[n][1]])
		j += 1
	else:
		currentmin = currentmin

ipcounter = 0

for i in range(0,len(consolidatedblocklist)-1):
	ipcounter += (consolidatedblocklist[i+1][0] - consolidatedblocklist[i][1] - 1)

print "Solution A: " + str(consolidatedblocklist[0][1] + 1)
print "Solution B: " + str(ipcounter)
