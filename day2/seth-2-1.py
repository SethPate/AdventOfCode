field = [(1, 2, 3), (4, 5, 6), (7, 8, 9)] #defines keypad

input_file = 'input.txt'

input1 = open(input_file, 'r')

content = input1.read()

content = content.split('\n')

print content

code = [] #what we need to enter

for i in field: #this shows the keypad
	print i

x = 1
y = 1

print 'starting at', (field[y][x]) # shows starting location

for i in content:
	print 'series is', i, 'starting at', field[y][x]
	for j in i:
		if j == 'U' and y != 0:
			y = y - 1
			print 'moving up to', field[y][x]
		if j == 'R' and x != 2:
			x = x + 1
			print 'moving right to', field[y][x]
		if j == 'D' and y != 2:
			y = y + 1
			print 'moving down to', field[y][x]
		elif j == 'L' and x != 0:
			x = x - 1
			print 'moving left to', field[y][x]
	code.append(field[y][x])
	print code 