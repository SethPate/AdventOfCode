from math import fabs
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

pin = ''
keypad = [
    ['x', 'x', '1', 'x', 'x'],
    ['x', '2', '3', '4', 'x'],
    ['5', '6', '7', '8', '9'],
    ['x', 'A', 'B', 'C', 'x'],
    ['x', 'x', 'D', 'x', 'x']
]
x, y = 0, 2

for step in steps:
    for i in range(len(step.rstrip('\n'))):
        char = step[i]
        if char == 'U':
            yi = max(0, y - 1)
            y = y if keypad[yi][x] == 'x' else yi
        elif char == 'D':
            yi = min(4, y + 1)
            y = y if keypad[yi][x] == 'x' else yi
        elif char == 'L':
            xi = max(0, x - 1)
            x = x if keypad[y][xi] == 'x' else xi
        elif char == 'R':
            xi = min(4, x + 1)
            x = x if keypad[y][xi] == 'x' else xi
    pin = pin + keypad[y][x]

print pin
