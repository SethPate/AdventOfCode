#dansolution15c

inputdata = "day15input.txt"

class Disc:
	name = ""
	currentposition = 0
	poscount = 0
	
	def discfacts(self):
		print "My name is %s. I am currently at position %s and I have %s total positions." % (self.name, self.currentposition, self.poscount)
	
	def incrementer(self):
		if self.currentposition + 1 == self.poscount:
			self.currentposition = 0
		else:
			self.currentposition += 1

def newlineimport(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.replace(".","")
	input1 = input1.split("\n")
	return input1

def lineup(a,b,c):
	if a.currentposition == b.currentposition + 1 + c or a.currentposition == (b.currentposition + 1 + c) % b.poscount:
		return "YES"
	else:
		return "NO"
	
disc_dict = {}

instructions = newlineimport(inputdata)

disc_names = []

for i in range(0,len(instructions)-1):
	instruction = instructions[i]
	instruction = instruction.split()
	discname = str(instruction[0]) + " " + str(instruction[1])
	disc_dict[discname] = Disc()
	disc_dict[discname].name = discname
	disc_dict[discname].currentposition = int(instruction[11])
	disc_dict[discname].poscount = int(instruction[3])
	disc_names.append(discname)

winner = 0
timevar = 0

while winner < len(disc_names) - 1:
	winner = 0
	for n in range(0,len(disc_names)-1):
		if lineup(disc_dict[disc_names[0]], disc_dict[disc_names[n+1]],n) == "YES":
			winner += 1
			
	for p in range(0,len(disc_names)):
		disc_dict[disc_names[p]].incrementer()
	timevar += 1
		
print timevar - 2
