from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
(opts, args) = parser.parse_args()

def parseLine(line):
	decomp = ''
	i = 0
	while i < len(line):
		if line[i] != '(':
			decomp += line[i]
			i += 1
		else:
			j = line.find(')', i)
			nc, nt = map(int,line[i+1:j].split('x'))
			i = j+1
			decomp += line[i:i+nc] * nt
			i += nc
	return decomp

with open(opts.inputfile, 'r') as f:
	for line in f:
		decomp = parseLine(line.rstrip('\n'))
		print len(decomp)
