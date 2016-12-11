from optparse import OptionParser
import re

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
(opts, args) = parser.parse_args()

def splitLine(line):
	inBrackets = [x.rstrip(']').lstrip('[') for x in re.findall(r'\[[a-z]+\]', line.rstrip('\n'))]
	outBrackets = re.sub(r'\[[a-z]+\]', ' ', line.rstrip('\n')).split()
	return [inBrackets, outBrackets]

def containsABBA(string):
	for i in range(3,len(string)):
		if (string[i-3] != string[i-2]) and (string[i-3:i-1] == string[i-1:i+1][::-1]):
			return True
	return False

def verifyLine(line):
	s = splitLine(line)
	inBrackets = any([containsABBA(x) for x in s[0]])
	outBrackets = any([containsABBA(x) for x in s[1]])
	return outBrackets and not inBrackets

with open(opts.inputfile,'r') as f:
	count = sum([verifyLine(line) for line in f.readlines()])

print count
