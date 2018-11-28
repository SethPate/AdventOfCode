#adventday1

directions = ["L4", "L3", "R1", "L4", "R2", "R2", "L1", "L2", "R1", "R1", "L3", "R5", "L2", "R5", "L4", "L3", "R2", "R2", "L5", "L1", "R4", "L1", "R3", "L3", "R5", "R2", "L5", "R2", "R1", "R1", "L5", "R1", "L3", "L2", "L5", "R4", "R4", "L2", "L1", "L1", "R1", "R1", "L185", "R4", "L1", "L1", "R5", "R1", "L1", "L3", "L2", "L1", "R2", "R2", "R2", "L1", "L1", "R4", "R5", "R53", "L1", "R1", "R78", "R3", "R4", "L1", "R5", "L1", "L4", "R3", "R3", "L3", "L3", "R191", "R4", "R1", "L4", "L1", "R3", "L1", "L2", "R3", "R2", "R4", "R5", "R5", "L3", "L5", "R2", "R3", "L1", "L1", "L3", "R1", "R4", "R1", "R3", "R4", "R4", "R4", "R5", "R2", "L5", "R1", "R2", "R5", "L3", "L4", "R1", "L5", "R1", "L4", "L3", "R5", "R5", "L3", "L4", "L4", "R2", "R2", "L5", "R3", "R1", "R2", "R5", "L5", "L3", "R4", "L5", "R5", "L3", "R1", "L1", "R4", "R4", "L3", "R2", "R5", "R1", "R2", "L1", "R4", "R1", "L3", "L3", "L5", "R2", "R5", "L1", "L4", "R3", "R3", "L3", "R2", "L5", "R1", "R3", "L3", "R2", "L1", "R4", "R3", "L4", "R5", "L2", "L2", "R5", "R1", "R2", "L4", "L4", "L5", "R3", "L4"]

setlength = len(directions)
z = 0
visitations = []

if directions[0][:1] == "L":
	orientation = 0
	x = int(directions[0][1:None]) * -1

else:
	orientation = 2
	x = int(directions[0][1:None])
	
endx = x
y = 0
endy = 0

#coordinate = str(x) + "," + str(y)
#visitations.append(coordinate)


#ORIENTATION

#FACING LEFT = 0
#FACING DOWN = 1
#FACING RIGHT = 2
#FACING UP = 3

for i in range(1,setlength):

	startx = endx
	starty = endy
	
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

	endy = y
	endx = x

	if endy == starty:
		k = startx
		
		while k != endx:
			if abs(endx - (k - 1)) < abs(endx - (k + 1)):
				k = k - 1
			else:
				k = k + 1
			coordinate = str(k) + "," + str(y)
			print coordinate
			if coordinate not in visitations:
				visitations.append(coordinate)
			else:
				print abs(k) + abs(y)
				exit()
			
	else:
		k = starty
		
		while k != endy:
			if abs(endy - (k - 1)) < abs(endy - (k + 1)):
				k = k - 1
			else:
				k = k + 1
			coordinate = str(x) + "," + str(k)
			print coordinate
			if coordinate not in visitations:
				visitations.append(coordinate)
			else:
				print abs(x) + abs(k)
				exit()
