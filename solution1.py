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

print(combined[0][0],combined[1][0])