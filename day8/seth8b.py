input1 = open('input.txt', 'r')
content = [i.strip() for i in input1.readlines()]

#test_content = ['rect 3x2','rotate column x=1 by 1','rotate row y=0 by 4','rotate column x=1 by 1']

screen = [range(0,50) for i in range(0,6)] #create the screen

for i in range(len(screen)): #set all pixels to 'off'
	for j in range(0,len(screen[i])):
		screen[i][j] = 0

#screen[0][0] = 1 #testing the push_row feature
#screen[5][0] = 1

#for i in screen: #now i finally have my screen!
#	print i

#at this point, i define the three functions we'll need for this project

def rectangle(string): #rectangle that is AxB; A wide (x) and B tall (y)
	string = string.split()
	string = string[1]
	string = string.split('x')
	x_bound = int(string[0]) #how wide
	y_bound = int(string[1]) #how deep
#	print 'a rectangle that is', x_bound, 'wide and', y_bound, 'deep'
	for i in range(0,y_bound): #turns on the correct pixels
		for j in range(0,x_bound):
			screen[i][j] = 1
#	print '\n' #returns the current screen
#	for i in screen:
#		print i

def push_row(string): #"rotate row" which pushes a certain row to the right, appending any "dropped" pixels back to the left
	string = string.split()
	string = string[len(string) - 3:len(string)]
	push = int(string[2]) #how far we're pushing it
	string[0] = string[0].split('=')
	row = int(string[0][1]) #which row we're pushing
#	print 'push row', row, 'by', push
	on_locations = []
	for i in range(0,len(screen[row])):
		if screen[row][i] == 1: #fchecks where the 1s are in the row
			on_locations.append(i)
#			print 'on at locations', on_locations
	for i in on_locations: #for each of those 1s
#		print 'pushing by', push
#		print i + push, len(string[row])
		if i + push < int(len(screen[row])): #if if wouldn't be pushed past the right
			screen[row][i + push] += 1 #increase the new location by one
			screen[row][i] -= 1 #decrease the old location by one
		else: #if it WOULD be pushed past the right,
			screen[row][push - (int(len(screen[row]) - i))] += 1 #increase the new location by one
			screen[row][i] -= 1 #decrease the old location by one
#	print '\n' #returns the current screen
#	for i in screen:
#		print i

def drop_col(string):
	string = string.split()
	drop = int(string[4]) #how far we're dropping the column
	string = string[2]
	string = string.split('=')
	col = int(string[1]) #which column i'm dropping
#	print 'drop', col, 'by', drop
	on_locations = []
	for i in range(0,len(screen)): #tell me which rows are 'on' in this column
		if screen[i][col] == 1:
			on_locations.append(i)
#	print 'on at locations', on_locations
	for i in on_locations: #for each of those locations,
#		print 'for location', i
		if (i + drop) < int(len(screen)): #if dropping wouldn't go past the bottom,
#			print 'no wrap because', i + drop, 'is less than', len(screen)
			screen[i + drop][col] += 1 #increase the new location by one
			screen[i][col] -= 1 #decrease the old location by one
#			print '\n'
#			for i in screen:
#				print i
		else: #if it WOULD go past the bottom
#			print 'wrap because', i + drop, 'is greater than or equal to', len(screen)
			screen[drop - (len(screen) - i)][col] += 1 #increase the new location by one
#			print 'now at', screen[drop - (len(screen) - i)][col]
			screen[i][col] -= 1 #decrease the old location by one
#	print '\n' #returns the current screen
#	for i in screen:
#		print i

#finally, i'll call each instruction (line of content) against one of three functions:

for i in content:
	if i[0:3] == 'rec': #this is the rectangle instruction
		rectangle(i)
	if i[7] == 'r': #this is the rotate row instruction
		push_row(i)
	if i[7] == 'c': #this is the rotate column instruction
		drop_col(i)

#now i need to add up the pixels...

summer = 0
for i in range(0,len(screen)):
	for j in range(0,len(screen[i])):
		summer += screen[i][j]

#print summer

#let's make them easier to read...

#for i in strings:
#	print '\r', i

#well, it's not 44.