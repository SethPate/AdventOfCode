class Floor(object):
	def __init__(self, level):
		self.level = level
		self.chips = []
		self.generators = []

	def addChip(self, chip):
		self.chips.append(chip)
		return self

	def addGenerator(self, gen):
		self.generators.append(gen)
		return self
