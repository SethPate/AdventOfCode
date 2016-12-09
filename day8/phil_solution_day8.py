import numpy as np
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
(opts, args) = parser.parse_args()

NR = 6
NC = 50
# NR = 3
# NC = 7

lcd = np.zeros((NR,NC), dtype=int)
rows = np.arange(NR, dtype=int)
cols = np.arange(NC, dtype=int)

def shiftRow(r, shift):
	lcd[r,:] = np.roll(lcd[r,:], shift)

def shiftCol(c, shift):
	lcd[:,c] = np.roll(lcd[:,c], shift)

def parseLine(line):
	s = line.rstrip('\n').split()
	if s[0] == 'rect':
		c, r = map(int, s[1].split('x'))
		lcd[:r,:c] = np.ones((r,c))
	elif s[0] == 'rotate':
		a, shift = int(s[2].split('=')[1]), int(s[4])
		if s[1] == 'row':
			lcd[a,:] = np.roll(lcd[a,:], shift)
		else:
			lcd[:,a] = np.roll(lcd[:,a], shift)

def printLCD():
	print('\n'.join(''.join('#' if p else ' '  for p in row) for row in lcd)+'\n')

with open(opts.inputfile, 'r') as f:
	for line in f:
		parseLine(line)

print lcd.sum()
print ''
printLCD()
