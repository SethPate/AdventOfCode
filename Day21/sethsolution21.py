#handle all squares as strings. only demux within functions, then mux in same.

def mux(square):
	#takes a list of strings, returns a string
	#use before each lookup
	# print('starting hashSquare with', square)
	squareString = ''
	for row in square:
		squareString += row
		squareString += '/'
	squareString = squareString[:-1]
	return squareString

def demux(square):
	#takes a string, gives a list of strings
	#use after each lookup
	return square.split('/')

def flip(square):
    #returns the mirror of the square
    square = demux(square)
    output = []
    for i in range(len(square)):
        row = square[i][::-1]
        output.append(row)
    output = mux(output)
    return output        

def r180(square):
	#returns the square rotated 180 degrees
    square = demux(square)
    flipSquare = []
    for i in range(1,len(square)+1):
        row = square[-i][::-1]
        flipSquare.append(row)
    flipSquare = mux(flipSquare)
    return flipSquare

def r90(square):
    #returns the square rotated 90 degrees
    square = demux(square)
    flipSquare = []
    for i in range(len(square[0])):
        row = ''
        for j in range(len(square)):
            row += (square[-(j+1)][i])
        flipSquare.append(row)
    flipSquare = mux(flipSquare)
    return flipSquare

def r270(square):
	#returns the square rotated 270 degrees
    return r180(r90(square))

def getRotations(square):
    #takes a string and returns a list of its rotations
    output = []
    output.append(square)
    output.append(r180(square))
    output.append(r90(square))
    output.append(r270(square))
    output.append(flip(square))
    output.append(flip(r180(square)))
    output.append(flip(r90(square)))
    output.append(flip(r270(square)))
    return output

def inputToDict(l):
	#parse all instructions into a dictionary
    output = {}
    for string in l:
        pieces = [i.strip() for i in string.split('=>')]
        output[pieces[0]] = pieces[1]
    return output

def divide(square):
	#divides a square into 2x2 or 3x3 squares, returns these as a list 
#    print('starting divider', square)
    square = demux(square)
    squares = []
    while square:
        newSquare = []
        newSquare.append(square[0][:2])
        newSquare.append(square[1][:2])
#        print('newSquare', newSquare)
        squares.append(newSquare)
        square[0] = square[0][2:]
        square[1] = square[1][2:]
        if len(square[0]) == 0:
            del square[0]
            del square[0]
    for i in range(len(squares)):
        squares[i] = mux(squares[i])
#    print('closing divider with', squares)
    return squares

def unpack(squares, instructions):
    #takes a list of squares
    #increases the square by one step
    #returns a list of the component squares
    output = []
    returnNew = False
    for i in squares:
        output.append(match(i,instructions))
    newoutput = []
    for i in output:
        if len(i) == 19: #if it's size 4 square
            returnNew = True
            littles = divide(i)
            print('divided', i, 'into', littles)
            for i in littles:
                newoutput.append(i)
    if returnNew == True:
        return newoutput
    else:
        return output

def match(square, instructions):
    #returns the square's match in instructions
    checker = getRotations(square)
    for i in checker:
        if i in instructions:
            worked = i
            output = instructions[i]
    print('matching', square, 'rotation', worked, 'to', output)
    return output

def count(squares):
    #takes a list of squares
    #returns the number of #s in them
    output = 0
    for i in squares:
        output += i.count('#')
    return output

prompt = ['.#./..#/###']

f = open('sethinput.txt','r')
data = f.read()
data = data.split('\n')

instructions = inputToDict(data)

print(prompt)

for i in range(1,6):
    print('iteration', i)
    prompt = unpack(prompt, instructions)
    print(prompt)
    print('length', len(prompt), 'count', count(prompt), '\n')