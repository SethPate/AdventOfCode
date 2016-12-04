import numpy as np
from optparse import OptionParser
import re

def getID(line):
	idstr = re.search("[0-9]+", line).group(0)
	return int(idstr)

def getTop5(line):
	return line.split(']')[0].split('[')[-1]

def isReal(line):
	letters = {}
	chars = line.split('[')[0].replace("-","")
	chars = re.sub("[0-9]+", "", chars)
	for c in chars:
		if c in letters:
			letters[c] = letters[c] + 1
		else:
			letters[c] = 1
	letterlist = []
	for l in letters:
		letterlist.append(Letter(l, letters[l]))
	letterlist.sort(cmp=compareLetters)
	top5 = ''
	for i in range(5):
		top5 = top5 + letterlist[i].letter
	return top5 == getTop5(line)

class Letter(object):
	letter = ''
	count = 0

	def __init__(self, letter, count):
		self.letter = letter
		self.count = count

	def __str__(self):
		return '{'+self.letter+','+str(self.count)+'}'

	def __repr__(self):
		return '{'+self.letter+','+str(self.count)+'}'

def compareLetters(l1, l2):
	if l1.count < l2.count:
		return 1
	elif l1.count > l2.count:
		return -1
	else:
		if l1.letter < l2.letter:
			return -1
		else:
			return 1

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
(opts, args) = parser.parse_args()

idsum = 0

infile = open(opts.inputfile, 'r')
for line in infile.readlines():
	if isReal(line):
		idsum += getID(line)

print idsum
