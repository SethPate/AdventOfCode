#dansolution12a

textimport = "day12input.txt"

def newlineimport(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.split("\n")
	return input1

#basic parser
def instructionparse(a):
	if a[0:3] == 'cpy':
		return "cpy"
	if a[0:3] == 'jnz':
		return "jnz"
	if a[0:3] == 'inc':
		return "inc"
	if a[0:3] == 'dec':
		return "dec"

#instructionprep

def cpysource(a):
	#print a
	a = a.split()
	return a[1]
	
def cpydestination(a):
	a = a.split()
	return a[2]

assembunny = newlineimport(textimport)
instructionnumber = 0
rega = 0
regb = 0
regc = 0
regd = 0

print len(assembunny)

while instructionnumber < len(assembunny) - 1:
	#print instructionnumber
	instruction = assembunny[instructionnumber]
	#print instruction
	if instructionparse(instruction) == 'cpy':
		#print instructionparse(instruction)
		sourcevar = cpysource(instruction)
		destinationvar = cpydestination(instruction)
		if sourcevar == "a":
			sourcevar = int(rega)
		elif sourcevar == "b":
			sourcevar = int(regb)
		elif sourcevar == "c":
			sourcevar = int(regc)
		elif sourcevar == "d":
			sourcevar = int(regd)
		else:
			sourcevar = sourcevar
		
		if destinationvar == "a": 
			rega = int(sourcevar)
		elif destinationvar == "b":
			regb = int(sourcevar)
		elif destinationvar == "c":
			regc = int(sourcevar)
		else:
			regd = int(sourcevar)
		
		instructionnumber += 1
		
	elif instructionparse(instruction) == 'inc':
		#print instructionparse(instruction)
		instruction = instruction.split()
		if instruction[1] == "a":
			rega += 1
		elif instruction[1] == "b":
			regb += 1
		elif instruction[1] == "c":
			regc += 1
		else:
			regd += 1
		
		instructionnumber += 1
	
	elif instructionparse(instruction) == 'dec':
		#print instructionparse(instruction)
		instruction = instruction.split()
		if instruction[1] == "a":
			rega -= 1
		elif instruction[1] == "b":
			regb -= 1
		elif instruction[1] == "c":
			regc -= 1
		else:
			regd -= 1 
		
		instructionnumber += 1
	
	elif instructionparse(instruction) == 'jnz':
		#print instructionparse(instruction)
		sourcevar = cpysource(instruction)
		#sourcevar = "a"
		destinationvar = cpydestination(instruction)
		#instructionnumber = 100
		#print "destinationvar = " + str(destinationvar)
		if sourcevar == "a":
			sourcevar = int(rega)
		elif sourcevar == "b":
			sourcevar = int(regb)
		elif sourcevar == "c":
			sourcevar = int(regc)
		elif sourcevar == "d":
			sourcevar = int(regd)
		else:
			sourcevar = sourcevar
		
		if destinationvar == "a":
			destinationvar = int(rega)
		elif destinationvar == "b":
			destinationvar = int(regb)
		elif destinationvar == "c":
			destinationvar = int(regc)
		elif destinationvar == "d":
			destinationvar = int(regd)
		else:
			destinationvar = destinationvar
		
		if sourcevar != 0:
			instructionnumber = instructionnumber + int(destinationvar)
		else:
			instructionnumber += 1
			
print rega
