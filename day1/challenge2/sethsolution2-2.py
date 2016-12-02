input_file = 'input1.txt'

input1 = open(input_file, 'r')

content = input1.read()

content = content.replace(" ", "")

content = content.split(',')

print (content)

#creating two variables for direction and distance

directions = []

distance = []

for i in content:
	directions.append(i[0])
	distance.append(i[1:])

#defining other variables

start = (0,0)

finish = [0,0]

locations = [] #this list will hold coordinates of all locations we've visited

bearing = "north"

north = 0
east = 0
south = 0
west = 0

#tracing the path

for index in content:
	print (index[0], index[1:])
	if bearing == "north":
		if index[0] == "R":
			print ("Turns east")
			xdif = int(index[1:])
			while xdif != 0:
				locations.append([int(finish[0]) + 1, finish[1]])
				finish[0] = finish[0] + 1
				xdif = xdif - 1
			print (finish)
			bearing = "east"
		else:
			print ("Turns west")
			xdif = -1 * int(index[1:])
			while xdif != 0:
				locations.append([int(finish[0]) - 1, finish[1]])
				finish[0] = finish[0] -1
				xdif = xdif + 1
			print (finish)
			bearing = "west"
	elif bearing == "east":
		if index[0] == "R":
			print ("Turns south")
			ydif = -1 * int(index[1:])
			while ydif != 0:
				locations.append([finish[0], int(finish[1]) - 1])
				finish[1] = finish[1] - 1
				ydif = ydif + 1
			print (finish)
			bearing = "south"
		else:
			print ("turns north")
			ydif = int(index[1:])
			while ydif != 0:
				locations.append([finish[0], int(finish[1]) + 1])
				finish[1] = finish[1] + 1
				ydif = ydif - 1
			finish[1] = finish[1] + int(index[1:])
			print (finish)
			bearing = "north"
	elif bearing == "south":
		if index[0] == "R":
			print ("turns west")
			xdif = -1 * int(index[1:])
			print (xdif)
			while xdif != 0:
				locations.append([int(finish[0]) - 1, finish[1]])
				finish[0] = finish[0] -1
				xdif = xdif + 1
			print (finish)
			bearing = "west"
		else:
			print ("turns east")
			xdif = int(index[1:])
			print ("xdif of " + str(xdif))
			while xdif != 0:
				locations.append([int(finish[0]) + 1, finish[1]])
				finish[0] = finish[0] + 1
				xdif = xdif - 1
			print (finish)
			bearing = "east"
	else:
		if index[0] == "R":
			print ("turns north")
			ydif = int(index[1:])
			while ydif != 0:
				locations.append([finish[0], int(finish[1]) + 1])
				finish[1] = finish[1] + 1
				ydif = ydif - 1
			print (finish)
			bearing = "north"
		else:
			print ("turns south")
			ydif = -1 * int(index[1:])
			while ydif != 0:
				locations.append([finish[0], int(finish[1]) - 1])
				finish[1] = finish[1] - 1
				ydif = ydif + 1			
			print (finish)
			bearing = "south"

# now i'm going to use a stupid method to find the first point of overlap

for i in locations:
	if locations.count(i) > 1:
		print (i, "Distance from finish: " + str(abs(i[0] - finish[0]) + abs(i[1] - finish[1])) + " steps")
		break

#and how far was it from the start?