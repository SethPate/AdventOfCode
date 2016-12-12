def isInt(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

class Bot(object):
	def __init__(self, btype, num):
		self.btype = btype
		self.num = num
		self.low_target = None
		self.high_target = None
		self.has = []

	def setMove(self, low_target, high_target):
		self.low_target = low_target
		self.high_target = high_target

	def getId(self):
		return self.btype+'_'+str(self.num)

	def receive(self, mc):
		self.has.append(mc)

	def process(self, botmap):
		if len(self.has) >= 2:
			low, high = min(self.has[0], self.has[1]), max(self.has[0], self.has[1])
			botmap[self.low_target].receive(low)
			botmap[self.high_target].receive(high)
			self.has.remove(low)
			self.has.remove(high)
			return True
		else:
			return False

	def __repr__(self):
		return self.getId()+' '+str(self.has)

	def __str__(self):
		return self.getId()+' '+str(self.has)

