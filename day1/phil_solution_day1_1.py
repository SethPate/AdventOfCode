from math import pi,sin,cos,fabs
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
(opts, args) = parser.parse_args()

steps = []

infile = open(opts.inputfile, 'r')
for line in infile.readlines():
	for step in line.split(','):
		steps.append(step.strip())
infile.close()

x = 0
y = 0
angle = pi/2
RIGHT = -pi/2
LEFT = pi/2

for step in steps:
	direction = step[0]
	distance = int(step[1:])
	if direction == 'R':
		angle += RIGHT
	elif direction == 'L':
		angle += LEFT
	else:
		print 'ERROR!'
		exit(-1)
	x += distance * cos(angle)
	y += distance * sin(angle)
	print x, y

print int(round(x)), int(round(y)), int(round(fabs(x)+fabs(y)))
