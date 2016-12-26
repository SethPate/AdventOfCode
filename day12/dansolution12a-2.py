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
	
	def cpyfunction(self, xinput, yinput):
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

assembunny = newlineimport(textimport)
instructionnumber = 0

myregistry = Registry()

myregistry.regdict["a"] = 0
myregistry.regdict["b"] = 0
myregistry.regdict["c"] = 0
myregistry.regdict["d"] = 0

while myregistry.instructionnumber < len(assembunny) - 1:
	instruction = assembunny[myregistry.instructionnumber]
	instruction = instruction.split()
	if instruction[0] == 'cpy':
		myregistry.cpyfunction(instruction[1], instruction[2])
	elif instruction[0] == 'inc':
		myregistry.incfunction(instruction[1])
	elif instruction[0] == 'dec':
		myregistry.decfunction(instruction[1])
	elif instruction[0] == 'jnz':
		myregistry.jnzfunction(instruction[1], instruction[2])

print myregistry.regdict["a"]
