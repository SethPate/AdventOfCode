#adventday3

#first, input the file as read only.
input_file = 'inputday3.txt'
input = open(input_file, 'r')

#put the text input into "triangles," and make "triangles" a list variable.
#the list variable splits at a new line.
triangles = input.read()
triangles = triangles.split("\n")

#a function for calculating impossible triangles.
def impossible(a,b,c):
	if (a + b > c) and (b + c > a) and (a + c > b):
		return "Valid!"
	else:
		return "Invalid!"

#initialize a counter
j = 0

#basic for loop for each element in triangles.
#parse out the information for each side, store in separate variables.
for i in range(0,len(triangles)-1):
	side1 = int(triangles[i][0:5].replace(" ",""))
	side2 = int(triangles[i][6:10].replace(" ",""))
	side3 = int(triangles[i][11:15].replace(" ",""))
	
	#run impossible function on triangles. increment counter j when valid.
	if impossible(side1,side2,side3) == "Valid!":
		j = j + 1

#display value of j after end of for loop.
print j
