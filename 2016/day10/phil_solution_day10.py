import re
from bot import *
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="inputfile", help="Input data file", default="input_phil.txt")
parser.add_option("-q", "--query", dest="query", action="append", help="Query numbers", default=[])
(opts, args) = parser.parse_args()

if len(opts.query) != 2 or not all(map(isInt, opts.query)):
	print "Invalid query! Must be exactly 2 numbers."
	exit(-1)

q = map(int, opts.query)
botmap = {}
valmap = {}

with open(opts.inputfile, 'r') as f:
	prog = re.compile('bot [0-9]+|output [0-9]+')
	for line in f.readlines():
		for s in prog.findall(line):
			t = s.split()
			bid = t[0]+'_'+t[1]
			if bid not in botmap:
				botmap[bid] = Bot(t[0], int(t[1]))
	
	f.seek(0)

	for line in f.readlines():
		t = line.split()
		if t[0] == 'value':
			botmap['bot_'+t[-1]].receive(int(t[1]))
		else:
			botmap[t[0]+'_'+t[1]].setMove(t[5]+'_'+t[6], t[10]+'_'+t[11])

	action = True
	while action:
		action = False
		for b in botmap:
			if q[0] in botmap[b].has and q[1] in botmap[b].has:
				print botmap[b]
			action = botmap[b].process(botmap) or action

for i in range(3):
	print botmap['output_'+str(i)]
