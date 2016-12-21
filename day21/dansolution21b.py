#dansolution21a

import random

inputtext = "day21input.txt"
passwordinput = "abcdefgh"
updatedpasswordlist = list(passwordinput)
passwordinputlist = list(passwordinput)

def newlineimport(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.split("\n")
	return input1

def interpreter(currentpassword,inputinstruction):
	stringlist = inputinstruction.split(" ")
	if stringlist[0] == "move":
		return moveinstruction(currentpassword,stringlist)
	elif stringlist[0] == "rotate":
		return rotateinstruction(currentpassword,stringlist)
	elif stringlist[0] == "swap":
		return swapinstruction(currentpassword,stringlist)
	elif stringlist[0] == "reverse":
		return reverseinstruction(currentpassword,stringlist)
	else:
		return "Invalid instruction."
		exit()

def moveinstruction(passwordlist,instruction):
	movefrom = int(instruction[2])
	moveto = int(instruction[5])
	moveholder = passwordlist.pop(movefrom)
	passwordlist.insert(moveto, moveholder)
	return passwordlist

def swapinstruction(passwordlist,instruction):
	if instruction[1] == "position":
		swap1 = int(instruction[2])
		swap2 = int(instruction[5])
	else:
		swap1 = passwordlist.index(instruction[2])
		swap2 = passwordlist.index(instruction[5])
	if swap1 >= swap2:
		moveholder1 = passwordlist.pop(swap1)
		moveholder2 = passwordlist.pop(swap2)
		passwordlist.insert(swap2,moveholder1)
		passwordlist.insert(swap1,moveholder2)
	else:
		moveholder1 = passwordlist.pop(swap2)
		moveholder2 = passwordlist.pop(swap1)
		passwordlist.insert(swap1,moveholder1)
		passwordlist.insert(swap2,moveholder2)
	return passwordlist

def reverseinstruction(passwordlist,instruction):
	reverse1 = int(instruction[2])
	reverse2 = int(instruction[4])
	reversedlist = []
	for n in range(reverse1,reverse2+1):
		reversedlist.append(passwordlist[n])
	reversedlist.reverse()
	for n in range(0,len(reversedlist)):
		passwordlist[reverse1+n] = reversedlist[n]
	return passwordlist

def rotateinstruction(passwordlist,instruction):
	rotator = 0
	if instruction[1] == "left":
		if instruction[2] != 0:
			rotator = int(instruction[2]) % len(passwordlist)
			return rotateleft(passwordlist,rotator)
		else:
			return passwordlist
	elif instruction[1] == "right":
		if instruction[2] != 0:
			rotator = int(instruction[2]) % len(passwordlist)
			return rotateright(passwordlist,rotator)
		else:
			return passwordlist
	else:
		positionmover = passwordlist.index(instruction[6]) + 1
		if positionmover >= 5:
			positionmover += 1
		rotator = positionmover % len(passwordlist)
		return rotateright(passwordlist,rotator)

def rotateleft(passwordlist,rotator):
	while rotator > 0:
		rotateme = passwordlist[0]
		del passwordlist[0]
		passwordlist.append(rotateme)
		rotator -= 1
	return passwordlist

def rotateright(passwordlist,rotator):
	while rotator > 0:
		rotateme = passwordlist[len(passwordlist)-1]
		del passwordlist[len(passwordlist)-1]
		passwordlist.insert(0, rotateme)
		rotator -= 1
	return passwordlist
	
instructions = newlineimport(inputtext)
instructions.remove("")

for i in range(0,len(instructions)):
	instruction = instructions[i]
	updatedpasswordlist = interpreter(updatedpasswordlist,instruction)

finalpassword = ""

for j in range(0,len(updatedpasswordlist)):
	finalpassword = finalpassword + str(updatedpasswordlist[j])

print "Solution A: " + finalpassword

#we're going to just brute-force solution B.

finalanswer = "fbgdceah"

counter = 0
previoustests = []
	
while finalanswer != finalpassword:
	finalpassword = ""
	testpasswordstring = ""
	testpassword = list(finalanswer)
	random.shuffle(testpassword)
	updatedpasswordlist = list(testpassword)
	if updatedpasswordlist not in previoustests:
		previoustests.append(updatedpasswordlist)

		for i in range(0,len(instructions)):
			instruction = instructions[i]
			updatedpasswordlist = interpreter(updatedpasswordlist,instruction)

		for j in range(0,len(updatedpasswordlist)):
			finalpassword = finalpassword + str(updatedpasswordlist[j])
	else:
		counter = counter
	counter += 1

for j in range(0,len(updatedpasswordlist)):
	testpasswordstring = testpasswordstring + str(testpassword[j])

print "Solution B: " + testpasswordstring
