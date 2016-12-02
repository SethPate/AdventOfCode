input_file = 'input1.txt'

input = open(input_file, 'r')

content = input.read()

content = content.replace(" ", "")

content = content.split(',')

directions = []

distance = []

combined = [directions, distance]

for i in content:
	directions.append(i[0])
	distance.append(i[1])

start = (0,0)

finish = (0,0)

bearing = "north"

north = 0
east = 0
south = 0
west = 0

for index in content:
	print (index[0])
	print (index[1])