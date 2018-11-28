from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
parser.add_option("-l", "--length", dest="length", help="Line length", default=None)
(opts, args) = parser.parse_args()

if opts.length is None:
	print "You need to provide a line length"
	exit(-1)

length = int(opts.length)

hists = []
for i in range(length):
	hists.append({})

with open(opts.inputfile) as f:
	for line in f:
		for i in range(length):
			if line[i] in hists[i]:
				hists[i][line[i]] += 1
			else:
				hists[i][line[i]] = 1

code1 = ''
code2 = ''
for i in range(length):
	hist_sort = sorted(hists[i].items(), key=lambda (k,v): (-v,k))
	code1 += hist_sort[0][0]
	code2 += hist_sort[-1][0]

print code1
print code2
