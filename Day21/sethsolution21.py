def hashSquare(square):
	#takes a list of strings, returns a string
	#use before each lookup
	# print('starting hashSquare with', square)
	squareString = ''
	for row in square:
		squareString += row
		squareString += '/'
	squareString = squareString[:-1]
	return squareString

def dehashSquare(square):
	#takes a string, gives a list of strings
	#use after each lookup
	return square.split('/')

def flip(square):
	#returns the square rotated 180 degrees
	flipSquare = []
	for i in range(1,len(square)+1):
		row = square[-i][::-1]
		flipSquare.append(row)
	return flipSquare

def right(square):
	#returns the square rotated 90 degrees
	flipSquare = []
	for i in range(len(square[0])):
		row = ''
		for j in range(len(square)):
			row += (square[-(j+1)][i])
		flipSquare.append(row)
	return flipSquare

def left(square):
	#returns the square rotated 270 degrees
	return flip(right(square))

def inputToDict(l):
	#parse all instructions into a dictionary
	output = {}
	for string in l:
		pieces = [i.strip() for i in string.split('=>')]
		output[pieces[0]] = pieces[1]
	return output

def increment(square, instructions):
	#break up the square into little bits, increase them, and put them back together
	if len(square[0]) < 4:
		return enhance(square, instructions)
	else:
		divided = divide(square)
		toUnite = []
		for square in divided:
			toUnite.append(enhance(square,instructions))
		return unite(toUnite)

def divide(square):
	#divides a square into 2x2 or 3x3 squares, returns these as a list 
	print('starting divider', square)
	if len(square) < 4:
		print('square length is less than 4, see', len(square), 'returning square')
		return square
	squares = []
	if len(square) % 3 == 0:
		divider = 3
	else:
		divider = 2
	while square:
		newSquare = []
		newSquare.append(square[0][:divider])
		newSquare.append(square[1][:divider])
		if divider == 3:
			newSquare.append(square[2][:divider])
		print('newSquare', newSquare)
		squares.append(newSquare)
		square[0] = square[0][divider:]
		square[1] = square[1][divider:]
		if divider == 3:
			square[2] = square[2][divider:]
		if len(square[0]) == 0:
			del square[0]
			del square[0]
			if divider == 3:
				del square[0]
	print('closing divider with', squares)
	return squares

def enhance(square, instructions):
	#increase size of an individual square
	print('calling enhance on', square)
	rotations = []
	rotations.append(hashSquare(square))
	rotations.append(hashSquare(flip(square)))
	rotations.append(hashSquare(right(square)))
	rotations.append(hashSquare(left(square)))
	print('full rotation list', rotations)
	for i in rotations:
		print('checking instructions for', i)
		if i in instructions:
			print('matching', i, 'to', instructions[i])
			newSquare = instructions[i]
	newSquare = dehashSquare(newSquare)
	print('enhance returning', newSquare)
	return newSquare

def unite(squares):
	#puts squares back together again!
	biggerSquare = []
	if len(squares[0]) % 3 == 0:
		uniter = 3
	else:
		uniter = 4
	for i in range(uniter*2):
		row = ''
		row += squares[0].pop(0)
		row += squares[1].pop(0)
		if not squares[0]:
			squares = squares[2:]
		print(i,row,squares)
		biggerSquare.append(row)
	return biggerSquare

f = open('sethinput.txt', 'r')
data = f.read()
data = data.split('\n')

instructions = inputToDict(data)

prompt = ['.#.','..#','###']

print(hashSquare(prompt))
print(hashSquare(flip(prompt)))
print(hashSquare(left(prompt)))
print(hashSquare(right(prompt)))

# for i in range(1,4):
# 	prompt = increment(prompt,instructions)
# 	print('increment', i, prompt)