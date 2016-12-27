#dansolution23a

textimport = "day23input.txt"

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

assembunny = newlineimport(textimport)

myregistry = Registry()

myregistry.regdict["a"] = 12
myregistry.regdict["b"] = 0
myregistry.regdict["c"] = 0
myregistry.regdict["d"] = 0

myregistry.instructions = assembunny
myregistry.instructions.remove("")
#print myregistry.instructions
counter = 0
#print len(assembunny)



while myregistry.instructionnumber < len(myregistry.instructions):
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
	#print myregistry.instructionnumber
	#print myregistry.instructions
	#print "a: " + str(myregistry.regdict["a"])
	#print "b: " + str(myregistry.regdict["b"])
	#print "c: " + str(myregistry.regdict["c"])
	#print "d: " + str(myregistry.regdict["d"])

#print myregistry.instructions
print myregistry.regdict["a"]
