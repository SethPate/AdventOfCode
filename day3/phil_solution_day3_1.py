import numpy as np
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
(opts, args) = parser.parse_args()

triangles = []

infile = open(opts.inputfile, 'r')
for line in infile.readlines():
	d = line.split()
	a = np.array([int(d[0]), int(d[1]), int(d[2])])
	a.sort()
	triangles.append(a)
infile.close()

count = 0
for t in triangles:
	if t[0]+t[1] > t[2]:
		count += 1

print count
