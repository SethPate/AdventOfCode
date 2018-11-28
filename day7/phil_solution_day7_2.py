from optparse import OptionParser
import re

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
(opts, args) = parser.parse_args()

def splitLine(line):
	inBrackets = [x.rstrip(']').lstrip('[') for x in re.findall(r'\[[a-z]+\]', line.rstrip('\n'))]
	outBrackets = re.sub(r'\[[a-z]+\]', ' ', line.rstrip('\n')).split()
	return [inBrackets, outBrackets]

def findABAs(string):
	aba = []
	for i in range(2,len(string)):
		if (string[i-2] != string[i-1]) and (string[i-2] == string[i]):
			aba.append(string[i-2:i+1])
	return aba

def matchBABs(string, aba):
	bab = aba[1]+aba[0]+aba[1]
	return bab in string

def verifyLine(line):
	s = splitLine(line)
	ABAs = [x for p in s[1] for x in findABAs(p)]
	return any([any([matchBABs(p, aba) for aba in ABAs]) for p in s[0]])

with open(opts.inputfile,'r') as f:
	count = sum([verifyLine(line) for line in f.readlines()])

print count
