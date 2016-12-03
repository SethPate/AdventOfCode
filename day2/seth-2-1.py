field = ['00100', '02340', '56789', '0ABC0', '00D00'] #defines keypad

input_file = 'input.txt'

input1 = open(input_file, 'r')

content = input1.read()

content = content.split('\n')

#content = ('ULL', 'RRDDD', 'LURDL', 'UUUUD')

print content

code = [] #what we need to enter

for i in field: #this shows the keypad
	print i

x = 0
y = 2

print 'starting at', (field[y][x]) # shows starting location

for i in content:
	print 'series is', i, 'starting at', field[y][x]
	for j in i:
		if j == 'U':
			if y - 1 > -1:
				if str(field[y - 1][x]) != '0':
					y = y - 1
					print 'moving up to', field[y][x]
		if j == 'R':
			if x < 4:
				if str(field[y][x + 1]) != '0':
					x = x + 1
					print 'moving right to', field[y][x]
		if j == 'D':
			if y < 4:
				if str(field[y + 1][x]) != '0':
					y = y + 1
					print 'moving down to', field[y][x]
		if j == 'L':
			if x - 1 > -1:
				if str(field[y][x - 1]) != '0':
					x = x - 1
					print 'moving left to', field[y][x]
	code.append(field[y][x])
	print code 