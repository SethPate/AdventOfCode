#dansolution10a

textimport = "day10input.txt"

class Bot:
	lowmicrochip = -1
	highmicrochip = -1
	lowinstruction = ""
	highinstruction = ""
	lowoutput = ""
	highoutput = ""
	twomicrochips = "no"
	receivedmicrochip = -1
	
	def valueadd(self,newchip):
		lchip = self.lowmicrochip
		hchip = self.highmicrochip
		if newchip > hchip:
			hchip = newchip
		else:
			lchip = newchip
		self.lowmicrochip = lchip
		self.highmicrochip = hchip
		
	def reorgchips(self):
		if int(self.receivedmicrochip) >= int(self.highmicrochip):
			self.lowmicrochip = self.highmicrochip
			self.highmicrochip = self.receivedmicrochip
		elif int(self.receivedmicrochip) < int(self.highmicrochip):
			self.lowmicrochip = self.receivedmicrochip
		else:
			self.highmicrochip = self.highmicrochip
	
	def chipcount(self):
		if self.lowmicrochip > -1 and self.highmicrochip > -1:
			self.twomicrochips = "yes"
		else:
			self.twomicrochips = "no"
	
	def test6117(self):
		if self.lowmicrochip == 17 and self.highmicrochip == 61:
			return "MATCH"
		
	def botdetails(self):
		desc_str = """This bot has a low microchip of %s and a 
		high microchip of %s. For its low instruction, 
		it goes to %s, and for its high instruction, it goes to %s.""" % (self.lowmicrochip, self.highmicrochip, self.lowinstruction, self.highinstruction)
		return desc_str

def importnolines(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.replace("\n","")
	return input1

def newlineimport(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.split("\n")
	return input1

def lowstring(a):
	b = a[a.find("gives low",0)+13:a.find(" ",a.find("gives low",0)+17)]
	if b == "output":
		b = a[a.find("gives low",0)+13:a.find(" ",a.find("gives low",0)+20)]
	return b

def highstring(a):
	b = a[a.find("and high",0)+12:]
	if b == "output":
		b = a[a.find("and high",0)+12:]
	return b
		
bot_dict = {}

botinstructions = importnolines(textimport)
n = 0
for n in range(0,len(botinstructions)):
	if botinstructions[n:n+3] == "bot":
		botnumber = botinstructions[n+4:botinstructions.find(" ",(n+4))]
		bot_dict["bot" + " " + str(botnumber)] = Bot()

botinstructions = newlineimport(textimport)
twochipper = []
botnamereceivelow = ""

for n in range(0,len(botinstructions)-1):
	botdirection = botinstructions[n]
	if botdirection[0:3] == "bot":
		botname = botdirection[0:botdirection.find(" ",5)]
		bot_dict[botname].lowinstruction = lowstring(botdirection)
		bot_dict[botname].highinstruction = highstring(botdirection)
	else:
		botdirection = botinstructions[n]
		i = 0
		if botdirection[i:i+3] != "bot":
			chipnumber = int(botdirection[6:botdirection.find(" ",7)])
			botname = botdirection[botdirection.find("bot"):]
			#print botname
			bot_dict[botname].valueadd(chipnumber)
			if bot_dict[botname].lowmicrochip > -1 and bot_dict[botname].highmicrochip > -1:
				twochipper.append(botname)

n = 0

sendingbot = twochipper[n]
outputs = {}

while n < (len(twochipper)):
	
	sendingbot = twochipper[n]
	#print n
	#print sendingbot
	
	if bot_dict[sendingbot].test6117() == "MATCH":
		print "Solution A: " + str(sendingbot)
	
	if bot_dict[sendingbot].lowinstruction[0:6] != "output":
		receiverlow = bot_dict[sendingbot].lowinstruction
		bot_dict[receiverlow].receivedmicrochip = bot_dict[sendingbot].lowmicrochip
		bot_dict[sendingbot].lowmicrochip = -1
		bot_dict[receiverlow].reorgchips()
		bot_dict[receiverlow].chipcount()
		if bot_dict[receiverlow].twomicrochips == "yes":
			twochipper.append(receiverlow)
			bot_dict[receiverlow].test6117()
	else:
		outputs[bot_dict[sendingbot].lowinstruction] = bot_dict[sendingbot].lowmicrochip 
	
	if bot_dict[sendingbot].highinstruction[0:6] != "output":
		receiverhigh = bot_dict[sendingbot].highinstruction
		bot_dict[receiverhigh].receivedmicrochip = bot_dict[sendingbot].highmicrochip
		#print bot_dict[receiverhigh].receivedmicrochip
		bot_dict[sendingbot].highmicrochip = -1
		bot_dict[receiverhigh].reorgchips()
		bot_dict[receiverhigh].chipcount()
		if bot_dict[receiverhigh].twomicrochips == "yes":
			twochipper.append(receiverhigh)
		bot_dict[receiverlow].test6117()
	else:
		outputs[bot_dict[sendingbot].highinstruction] = bot_dict[sendingbot].highmicrochip
		
	n = n + 1

print "Solution B: " + " " + str(outputs.get('output 0') * outputs.get('output 1') * outputs.get('output 2'))
