input_file = 'input.txt'

input1 = open(input_file, 'r')

content = input1.readlines()

#need to split these lines up!

print content[0] #here's what i'm starting with

a = content[0] #defining a string with the contents

print a #making sure that it works

a = a.split()

print a #hey, that did it!

realtrianglecounter = 0 #because this is what our answer will be

#let's turn this into an engine for each line now

for i in content:
	a = i.split()
	print a
	side1 = int(a[0]) #now to get the sides defined...
	side2 = int(a[1])
	side3 = int(a[2])
	largestside = max(side1,side2,side3) #which one is biggest?
	sumofothers = side1 + side2 + side3 - largestside #now the smaller ones...
	if largestside < sumofothers: #if it's fake
		realtrianglecounter = realtrianglecounter + 1 #keeping tally
		print a, 'this is a triangle!' #verbose for no reason

print realtrianglecounter
