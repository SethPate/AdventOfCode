from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
(opts, args) = parser.parse_args()

def parseLine(line):
	length = 0
	i = 0
	while i < len(line):
		if line[i] != '(':
			i += 1
			length += 1
		else:
			j = line.find(')', i)
			nc, nt = map(int,line[i+1:j].split('x'))
			i = j+1
			length += parseLine(line[i:i+nc]) * nt
			i += nc
	return length

with open(opts.inputfile, 'r') as f:
	for line in f:
		print parseLine(line.rstrip('\n'))
