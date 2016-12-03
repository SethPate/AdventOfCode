#adventday2

input_file = 'day2input.txt'

input = open(input_file, 'r')

buttonorders = input.read()
buttonorders = buttonorders.split("\n")

setlength = len(buttonorders)

def keypadmove(a,b):
	if b == "U":
		if a == 1:
			return 1
		elif a == 2:
			return 2
		elif a == 3:
			return 3
		else:
			return a - 3
	elif b == "D":
		if a == 7:
			return 7
		elif a == 8:
			return 8
		elif a == 9:
			return 9
		else:
			return a + 3
	elif b == "L":
		if a == 1:
			return 1
		elif a == 4:
			return 4
		elif a == 7:
			return 7
		else:
			return a - 1
	elif b == "R":
		if a == 3:
			return 9
		elif a == 6:
			return 6
		elif a == 9:
			return 9
		else:
			return a + 1
	
	else:
		return 0

keynum = 5
keystring = ""

for i in range(0,setlength - 1):
	for j in range(0,len(buttonorders[i])):
		keynum = keypadmove(keynum,	buttonorders[i][j:(j+1)])
		
	keystring = keystring + str(keynum)

print keystring
