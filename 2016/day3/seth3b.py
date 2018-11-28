#input section

input_path = 'input.txt'

input_file = open(input_path, 'r')

content = input_file.readlines()

"""
test content
"""

#content = content[:6]

#for i in content:
#	print i

"""

line1 will be 2:5
line2 will be 7:10
line3 will be 12:15

"""

line1 = []
line2 = []
line3 = []

for i in content:
	line1.append(i[2:5])
	line2.append(i[7:10])
	line3.append(i[12:15])

lines = [line1, line2, line3]

print 'superset of lines', lines

"""
now i've got the rows into their own strings,
so i'm going to figure out some way to sort them into 3s.
"""

triangle_list = []

for i in lines:
	#print 'this is the i', i
	counter = 3
	for j in i:
		#print 'this is the j', j
		if counter <= len(i):
			triangle_list.append(i[counter - 3:counter])
			counter = counter + 3
			#print 'current triangle list', triangle_list

print 'ordered into triangles', triangle_list

"""
and now, the simple triangle checking engine from day3a
"""

correct_triangles = 0

for i in triangle_list:
	side1 = int(i[0])
	side2 = int(i[1])
	side3 = int(i[2])
	longest = max(side1,side2,side3)
	if longest < side1 + side2 + side3 - longest:
		correct_triangles = correct_triangles + 1

print correct_triangles
