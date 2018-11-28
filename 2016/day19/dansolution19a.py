#dansolution19a

numberofelves = 3001330

y = 0
x = 2

while x < numberofelves:	
	x *= 2
	y += 1

if numberofelves == 2 * (numberofelves - (2 ** y)):
	print 1
else:
	print 2 * (numberofelves - (2 ** y)) + 1
