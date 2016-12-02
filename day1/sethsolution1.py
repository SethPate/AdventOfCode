input_file = 'input1.txt'

input = open(input_file, 'r')

content = input.read()

content = content.replace(" ", "")

content = content.split(',')

directions = []

distance = []

for i in content:
	directions.append(i[0])
	distance.append(i[1:])

start = (0,0)

finish = [0,0]

bearing = "north"

north = 0
east = 0
south = 0
west = 0

stepcounter = 0

print ("Bearing is " + bearing)

for index in content:
	print (index[0], index[1:])
	stepcounter = stepcounter + 1
	print (stepcounter)
	if bearing == "north":
		if index[0] == "R":
			print ("Turns east")
			finish[0] = finish[0] + int(index[1:])
			print (finish)
			bearing = "east"
		else:
			print ("Turns west")
			finish[0] = finish[0] - int(index[1:])
			print (finish)
			bearing = "west"
	elif bearing == "east":
		if index[0] == "R":
			print ("Turns south")
			finish[1] = finish[1] - int(index[1:])
			print (finish)
			bearing = "south"
		else:
			print ("turns north")
			finish[1] = finish[1] + int(index[1:])
			print (finish)
			bearing = "north"
	elif bearing == "south":
		if index[0] == "R":
			print ("turns west")
			finish[0] = finish[0] - int(index[1:])
			print (finish)
			bearing = "west"
		else:
			print ("turns east")
			finish[0] = finish[0] + int(index[1:])
			print (finish)
			bearing = "east"
	else:
		if index[0] == "R":
			print ("turns north")
			finish[1] = finish[1] + int(index[1:])
			print (finish)
			bearing = "north"
		else:
			print ("turns south")
			finish[1] = finish[1] - int(index[1:])
			print (finish)
			bearing = "south"

print (abs(finish[0] - start[0]) + abs(finish[1] - start[1]))

print ("number of steps: " + str(len(content)))

print (distance)