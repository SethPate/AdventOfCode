#dansolution22a

textinput = "day22input.txt"

def newlineimport(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	while "  " in input1:
		input1 = input1.replace("  "," ")
	input1 = input1.split("\n")
	return input1

class Nodes:
	name = ""
	xpos = ""
	ypos = ""
	size = ""
	used = ""
	avail = ""
	
	def nodedescription(self):
		desc_str = """I'm node %s, with an x-position of %s and a
y-position of %s. I hold %s units of space and have used %s,
so I have %s units available.""" % (self.name, self.xpos, self.ypos, self.size, self.used, self.avail)
		return desc_str

nodelist = newlineimport(textinput)
nodelist.remove("")

node_dict= {}

for i in range(2,len(nodelist)):
	nodedetails = nodelist[i].split(" ")
	nodename = nodedetails[0]
	node_dict[nodename] = Nodes()
	node_dict[nodename].name = nodename
	node_dict[nodename].xpos = int(nodename[(nodename.find("x",0)+1):nodename.find("-",nodename.find("x",0))])
	node_dict[nodename].ypos = int(nodename[(nodename.find("y",0)+1):])
	node_dict[nodename].size = int(nodedetails[1].replace("T",""))
	node_dict[nodename].used = int(nodedetails[2].replace("T",""))
	node_dict[nodename].avail = int(nodedetails[3].replace("T",""))

counter = 0

for a in range(2,len(nodelist)):
	nodedetails = nodelist[a].split(" ")
	nodenamea = nodedetails[0]
	for b in range(2,len(nodelist)):
		nodedetails = nodelist[b].split(" ")
		nodenameb = nodedetails[0]
		if node_dict[nodenamea].used != 0:
			if node_dict[nodenamea].name != node_dict[nodenameb].name:
				if node_dict[nodenamea].used <= node_dict[nodenameb].avail:
					counter += 1

print counter
