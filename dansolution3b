#adventday3

#a function for calculating impossible triangles.
def impossible(a,b,c):
	if (a + b > c) and (b + c > a) and (a + c > b):
		return "Valid!"
	else:
		return "Invalid!"

#initialize a counter
j = 0

#input the file as read only.
input_file = 'inputday3.txt'
input = open(input_file, 'r')

#put the text input into "triangles," and make "triangles" a list variable.
#the list variable splits at a new line.
triangles = input.read()

#set up some lists
triangles1 = []
triangles2 = []
triangles3 = []

#get the first line into the lists
triangles1.append(triangles[0:5])
triangles2.append(triangles[6:11])
triangles3.append(triangles[12:17])

#at every line break, append the next few characters into each list.
for i in range(0,len(triangles)):
	if triangles[i:i+1] == "\n":
		triangles1.append(triangles[i+1:i+6])
		triangles2.append(triangles[i+7:i+12])
		triangles3.append(triangles[i+13:i+18])

#remove spaces, convert into integers.
for i in range(0,len(triangles1)-1):
	triangles1[i] = int(triangles1[i].replace(" ",""))
	triangles2[i] = int(triangles2[i].replace(" ",""))
	triangles3[i] = int(triangles3[i].replace(" ",""))

#print triangles2

#for loop using a MOD function. Every set of 3 lines should be checked.
#When the remainder of divide by 3 = 0, then run the impossible formula.
for i in range(0,len(triangles1)-1):
	if (i + 6) % 3 == 0:
		if impossible(triangles1[i],triangles1[i+1],triangles1[i+2]) == "Valid!":
			j = j + 1
		if impossible(triangles2[i],triangles2[i+1],triangles2[i+2]) == "Valid!":
			j = j + 1
		if impossible(triangles3[i],triangles3[i+1],triangles3[i+2]) == "Valid!":
			j = j + 1
		
print j
