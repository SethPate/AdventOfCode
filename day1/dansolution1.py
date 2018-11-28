#adventday1

directions = ["L4", "L3", "R1", "L4", "R2", "R2", "L1", "L2", "R1", "R1", "L3", "R5", "L2", "R5", "L4", "L3", "R2", "R2", "L5", "L1", "R4", "L1", "R3", "L3", "R5", "R2", "L5", "R2", "R1", "R1", "L5", "R1", "L3", "L2", "L5", "R4", "R4", "L2", "L1", "L1", "R1", "R1", "L185", "R4", "L1", "L1", "R5", "R1", "L1", "L3", "L2", "L1", "R2", "R2", "R2", "L1", "L1", "R4", "R5", "R53", "L1", "R1", "R78", "R3", "R4", "L1", "R5", "L1", "L4", "R3", "R3", "L3", "L3", "R191", "R4", "R1", "L4", "L1", "R3", "L1", "L2", "R3", "R2", "R4", "R5", "R5", "L3", "L5", "R2", "R3", "L1", "L1", "L3", "R1", "R4", "R1", "R3", "R4", "R4", "R4", "R5", "R2", "L5", "R1", "R2", "R5", "L3", "L4", "R1", "L5", "R1", "L4", "L3", "R5", "R5", "L3", "L4", "L4", "R2", "R2", "L5", "R3", "R1", "R2", "R5", "L5", "L3", "R4", "L5", "R5", "L3", "R1", "L1", "R4", "R4", "L3", "R2", "R5", "R1", "R2", "L1", "R4", "R1", "L3", "L3", "L5", "R2", "R5", "L1", "L4", "R3", "R3", "L3", "R2", "L5", "R1", "R3", "L3", "R2", "L1", "R4", "R3", "L4", "R5", "L2", "L2", "R5", "R1", "R2", "L4", "L4", "L5", "R3", "L4"]

setlength = len(directions)

if directions[0][:1] == "L":
	orientation = 0
	x = int(directions[0][1:None]) * -1

else:
	orientation = 2
	x = int(directions[0][1:None])
	
y = 0

#ORIENTATION

#FACING LEFT = 0
#FACING DOWN = 1
#FACING RIGHT = 2
#FACING UP = 3

for i in range(1,setlength):

	turn = directions[i][:1]
	distance = int(directions[i][1:None])
	
	if orientation == 0:
		if turn == "L":
			y = y - distance
			orientation = 1
		else:
			y = y + distance
			orientation = 3
	
	elif orientation == 1:
		if turn == "L":
			x = x + distance
			orientation = 2
		else:
			x = x - distance
			orientation = 0
	
	elif orientation == 2:
		if turn == "L":
			y = y + distance
			orientation = 3
		else:
			y = y - distance
			orientation = 1
	
	else:
		if turn == "L":
			x = x - distance
			orientation = 0
		else:
			x = x + distance
			orientation = 2

print x + y
