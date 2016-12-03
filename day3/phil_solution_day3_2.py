import numpy as np

triangles = []

infile = open('input_phil.txt', 'r')
data = infile.readlines()
for i in range(0,len(data),3):
	d1 = data[i].split()
	d2 = data[i+1].split()
	d3 = data[i+2].split()
	for j in range(3):
		a = np.array([int(d1[j]), int(d2[j]), int(d3[j])])
		a.sort()
		triangles.append(a)
infile.close()

count = 0
for t in triangles:
	if t[0]+t[1] > t[2]:
		count += 1

print count
