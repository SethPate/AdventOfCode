from math import pi,sin,cos,fabs

steps = []

infile = open('input_phil.txt', 'r')
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
