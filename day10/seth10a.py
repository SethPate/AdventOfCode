import sys

content = [i.strip() for i in open('input.txt').readlines()]

#content = ['value 15 goes to bot 2',
#			'bot 2 gives low to bot 1 and high to bot 0',
#			'value 13 goes to bot 1',
#			'bot 1 gives low to output 1 and high to bot 0',
#			'bot 0 gives low to output 2 and high to output 0',
#			'value 12 goes to bot 2']

#above is test content

class Bot(object):

	def __init__(self, name, chips, lowpoint, low, highpoint, high):
		self.name = name
		self.chips = []
		self.lowpoint = lowpoint #output or bot
		self.low = low #number of lowpoint
		self.highpoint = highpoint #output or bot
		self.high = high #number of lowpoint

	def say_chips(self):
		print "i have these chips", self.chips

	def give_chips(self):
		if len(self.chips) == 2:
			chip_l = sorted(self.chips)
			low_chip = chip_l[0]
			high_chip = chip_l[1]
			print 'bot', self.name, 'has', chip_l
			if '17' in chip_l and '61' in chip_l:
				print 'the answer is bot', self.name, 'because i have chips', self.chips
#				sys.exit()
			print 'starting to give chips: i am bot', self.name, 'giving low chip', low_chip, 'to', self.lowpoint, self.low, 'and my high chip', high_chip, 'to', self.highpoint, self.high
			for i in chip_l:
				if i == low_chip:
					if self.lowpoint == 'bot':
						bot_d[self.low].chips.append(low_chip)
						self.chips.remove(low_chip)
						iterator.append(self.low)
						print iterator
					else: 
						out_d[self.low].chips.append(low_chip)
						self.chips.remove(low_chip)
				else:
					if self.highpoint == 'bot':
						bot_d[self.high].chips.append(high_chip)
						self.chips.remove(high_chip)
						iterator.append(self.high)
						print iterator
					else:
						out_d[self.high].chips.append(high_chip)
						self.chips.remove(high_chip)
			print "this is bot", self.name, "whose chips are gone now, remaining chips:", self.chips
		else:
			print "received a chip but holding: this is bot", self.name, 'and i have only one chip which is', self.chips

class Output(object):

	def __init__(self, chips):
		self.chips = []

bot_d = {}
out_d = {}
iterator = []

instructions = [i for i in content if i[0] == 'v'] #this is a list of all instructions which deal with inputs

print instructions

for i in content: #go through the instructions to build all the bots
	i = i.split()
	if i[0] == 'bot': #if it's a bot instruction
		bot_d[i[1]] = Bot(i[1],[0,0],i[5],i[6],i[10],i[11]) #then create a Bot object with that bot's number
		if i[5] == 'output': #if it gives to output
			out_d[i[6]] = Output([])
		if i[10] == 'output': #if it gives to output
			out_d[i[11]] = Output([])

#print bot_d
#print out_d

for i in instructions:
	print i
	i = i.split()
	bot_d[i[5]].chips.append(i[1])
#	print 'bot', i[5], 'has', bot_d[i[5]].chips
#	if len(bot_d[i[5]].chips) > 1:
	bot_d[i[5]].give_chips()

for i in iterator:
	bot_d[i].give_chips()

#it's not bot 38.

#print out_d['0'].chips, out_d['1'].chips, out_d['2'].chips
#print bot_d['0'].chips, bot_d['1'].chips, bot_d['2'].chips