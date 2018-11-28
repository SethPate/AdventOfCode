#dansolution23a

textimport = "day25input.txt"

def newlineimport(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.split("\n")
	return input1
		
class Registry:
	regdict = {}
	instructionnumber = 0
	instructions = []
	
	def cpyfunction(self, xinput, yinput):
		if yinput.lstrip("-").isdigit() is False:
			if xinput.lstrip("-").isdigit() is False:
				sender = int(self.regdict[xinput])
			else:
				sender = int(xinput)
			self.regdict[yinput] = sender
		self.instructionnumber += 1
	
	def incfunction(self, xinput):
		self.regdict[xinput] += 1
		self.instructionnumber += 1
	
	def decfunction(self, xinput):
		self.regdict[xinput] -= 1
		self.instructionnumber += 1
	
	def jnzfunction(self, xinput, yinput):
		if yinput.lstrip("-").isdigit() is False:
			yinput = self.regdict[yinput]
		if xinput.lstrip("-").isdigit() is True:
			if int(xinput) != 0:
				self.instructionnumber += int(yinput)
			else:
				self.instructionnumber += 1
		else:
			if int(self.regdict[xinput]) != 0:
				self.instructionnumber += int(yinput)
			else:
				self.instructionnumber += 1
		
	def tglfunction(self, xinput):
		if xinput.lstrip("-").isdigit() is False:
			xinput = int(self.regdict[xinput])
		toggledinstrnum = self.instructionnumber + int(xinput)
		if toggledinstrnum < len(self.instructions):
			changer = self.instructions[toggledinstrnum]
			changer = changer.split()
			if len(changer) == 2:
				if changer[0] == 'inc':
					newinstruction = "dec " + changer[1]
				else:
					newinstruction = "inc " + changer[1]
			if len(changer) == 3:
				if changer[0] == 'jnz':
					newinstruction = "cpy " + changer[1] + " " + changer[2]
				else:
					newinstruction = "jnz " + changer[1] + " " + changer[2]
			self.instructions[toggledinstrnum] = newinstruction
		self.instructionnumber += 1
	
	def outfunction(self,xinput):
		if xinput.lstrip("-").isdigit() is False:
			xinput = int(self.regdict[xinput])
		self.instructionnumber += 1
		return xinput

assembunny = newlineimport(textimport)

myregistry = Registry()

myregistry.regdict["a"] = 0
myregistry.regdict["b"] = 0
myregistry.regdict["c"] = 0
myregistry.regdict["d"] = 0

myregistry.instructions = assembunny
myregistry.instructions.remove("")
counter = 0
startinga = 0

while counter != 1:

	myregistry.regdict["a"] = 0
	myregistry.regdict["b"] = 0
	myregistry.regdict["c"] = 0
	myregistry.regdict["d"] = 0
	myregistry.instructionnumber = 0
	testerlist = []
	startinga += 1
	
	myregistry.regdict["a"] = startinga
	testme = "PASS"
	n = 0
	
	while len(testerlist) < 13 and testme != "FAIL":
		instruction = myregistry.instructions[myregistry.instructionnumber]
		instruction = instruction.split()
		if instruction[0] == 'cpy':
			myregistry.cpyfunction(instruction[1], instruction[2])
		elif instruction[0] == 'inc':
			myregistry.incfunction(instruction[1])
		elif instruction[0] == 'dec':
			myregistry.decfunction(instruction[1])
		elif instruction[0] == 'jnz':
			myregistry.jnzfunction(instruction[1], instruction[2])
		elif instruction[0] == 'tgl':
			myregistry.tglfunction(instruction[1])
		elif instruction[0] == 'out':
			testerlist.append(myregistry.outfunction(instruction[1]))
			if len(testerlist) > 1 and testerlist[n] == testerlist[n-1]:
				testme = "FAIL"
			n += 1

		if len(testerlist) > 10 and testme == "PASS":
			print "25A: " + str(startinga)
			exit()
