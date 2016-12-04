import numpy as np
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
(opts, args) = parser.parse_args()

triangles = []

infile = open(opts.inputfile, 'r')
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
