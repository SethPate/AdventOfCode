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
			return 1
		elif a == 4:
			return 4
		elif a == 5:
			return 5
		elif a == "A":
			return 6
		elif a == "B":
			return 7
		elif a == "C":
			return 8
		elif a == "D":
			return "B"
		else:
			return a - 4
	elif b == "D":
		if a == 1:
			return 3
		elif a == 5:
			return 5
		elif a == 9:
			return 9
		elif a == 6:
			return "A"
		elif a == 7:
			return "B"
		elif a == 8:
			return "C"
		elif a == 9:
			return 9
		elif a == "D":
			return "D"
		elif a == "A":
			return "A"
		elif a == "B":
			return "D"
		elif a == "C":
			return "C"
		else:
			return a + 4
	elif b == "L":
		if a == 1:
			return 1
		elif a == 2:
			return 2
		elif a == 5:
			return 5
		elif a == "C":
			return "B"
		elif a == "A":
			return "A"
		elif a == "B":
			return "A"
		elif a == "D":
			return "D"
		else:
			return a - 1
	elif b == "R":
		if a == 1:
			return 1
		elif a == 4:
			return 4
		elif a == 9:
			return 9
		elif a == "C":
			return "C"
		elif a == "A":
			return "B"
		elif a == "B":
			return "C"
		elif a == "D":
			return "D"
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
