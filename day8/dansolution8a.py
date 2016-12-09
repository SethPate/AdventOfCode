#dansolution8a

textimport = 'day8input.txt'

def newlinefilenospaces(a):
	input1 = open(a, 'r')
	input1 = input1.read()
	input1 = input1.replace(" ","")
	input1 = input1.split("\n")
	return input1

def runprocedure(c,d):
	if d[0:4] == "rect":
		a = int(d[(d.find("t")+1):(d.find("x"))])
		b = int(d[(d.find("x") + 1):])
		return rectAB(a,b,c)
	elif d[0:13] == "rotatecolumnx":
		a = int(d[(d.find("=")+1):(d.find("by"))])
		b = int(d[(d.find("by") + 2):])
		return rotatecolXAB(a,b,c)
	elif d[0:10] == "rotaterowy":
		a = int(d[(d.find("=")+1):(d.find("by"))])
		b = int(d[(d.find("by") + 2):])
		return rotaterowYAB(a,b,c)
	else:
		exit()
	return c		

def rectAB(a,b,c):
	for i in range(0,b):
		for j in range(0,a):
			c[i][j:j+1] = '#'
	return c

def rotaterowYAB(a,b,c):
	d = []
	d = rowfall(a,b,c)
	e = []
	e = rowrise(a,b,c)
	for i in range(0,len(d)):
		c[a][i] = d[i]
	j = 0
	for i in range(len(d),screenwidth):	
		c[a][i] = e[j]
		j += 1
	return c

def rowfall(a,b,c):
	d = []
	for i in range(0,screenwidth):
		if b + i > screenwidth - 1:
			d.append(c[a][i])
	return d

def rowrise(a,b,c):
	e = []
	for i in range(0,screenwidth-b):
		if b + i <= screenwidth - 1:
			e.append(c[a][i])
	return e

def rotatecolXAB(a,b,c):
	d = []
	d = colfall(a,b,c)
	e = []
	e = colrise(a,b,c)
	for i in range(0,len(d)):
		c[i][a] = d[i]
	j = 0
	for i in range(len(d),screenheight):
		c[i][a] = e[j]
		j += 1
	return c

def colfall(a,b,c):
	d = []
	for i in range(0,screenheight):
		if b + i > screenheight - 1:
			d.append(c[i][a])
	return d

def colrise(a,b,c):
	e = []
	for i in range(0,screenheight-b):
		if b + i <= screenheight - 1:
			e.append(c[i][a])
	return e

def screensize(a,b):
	screen1 = []
	screen1 = [[] for i in range(b)]
	for j in range(0,b):
		for i in range(0,a):
			screen1[j].append('.')
	return screen1

screenwidth = 50
screenheight = 6

screen = screensize(screenwidth,screenheight)

screeninstructions = newlinefilenospaces(textimport)

for n in range(0,len(screeninstructions)-1):
	screen = runprocedure(screen,screeninstructions[n])

print sum(x.count("#") for x in screen)

#Part B
letterlist = screensize(5,6)

for n in range(0,10):
	for i in range(0,6):
		for j in range(0,5):
			letterlist[i][j] = screen[i][j+(n*5)]
		print letterlist[i]
	print "break!"
