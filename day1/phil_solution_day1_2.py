from math import pi,sin,cos,fabs
from optparse import OptionParser

def checkLocation(p, locations):
	for l in locations:
		if p[0] == l[0] and p[1] == l[1]:
			return True
	return False

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

locations = []
end = None

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
	xs = int(round(x))
	ys = int(round(y))
	x += distance * cos(angle)
	y += distance * sin(angle)
	for i in range(distance):
		l = [int(round(xs + i * cos(angle))), int(round(ys + i * sin(angle)))]
		if not checkLocation(l, locations):
			locations.append(l)
		elif end is None:
			end = l

print int(round(x)), int(round(y)), int(round(fabs(x)+fabs(y)))

print end, int(round(fabs(x-end[0])+fabs(y-end[1]))), int(round(fabs(end[0])+fabs(end[1])))


