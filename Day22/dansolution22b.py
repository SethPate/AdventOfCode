#dansolution22

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    if '' in input1:
        input1.remove('')
    return input1

def listoflists(a):
    for b in range(0,len(a)):
        a[b] = list(a[b])
    return a

#turning functions
def rightturn(direction):
    if direction == 'u':
        return 'r'
    elif direction == 'r':
        return 'd'
    elif direction == 'd':
        return 'l'
    elif direction == 'l':
        return 'u'
    else:
        return "ERROR"

def leftturn(direction):
    if direction == 'u':
        return 'l'
    elif direction == 'l':
        return 'd'
    elif direction == 'd':
        return 'r'
    elif direction == 'r':
        return 'u'
    else:
        return "ERROR"

def reverse(direction):
    if direction == 'u':
        return 'd'
    elif direction == 'l':
        return 'r'
    elif direction == 'd':
        return 'u'
    elif direction == 'r':
        return 'l'
    else:
        return "ERROR"

def turnme(position,direction):
    if position == '#':
        direction = rightturn(direction)
    elif position == '.':
        direction = leftturn(direction)
    elif position == 'F':
        direction = reverse(direction)
    return direction

#infection
def infection(position):
    if position == '#':
        position = 'F'
    elif position == 'F':
        position = '.'
    elif position == '.':
        position = 'W'
    else:
        position = '#'
    return position

#movement
def movement(xposition,yposition,direction):
    poslist = []
    if direction == 'u':
        yposition -= 1
    elif direction == 'r':
        xposition += 1
    elif direction == 'd':
        yposition += 1
    elif direction == 'l':
        xposition -= 1
    poslist.append(xposition)
    poslist.append(yposition)
    return poslist

def gridexpandy(grid,ypos):
    gridwidth = len(grid[0])
    gridheight = len(grid)
    gridrow = []
    for a in range(0,gridwidth):
        gridrow.append('.')
    if ypos < 0:
        grid.insert(0, gridrow)
    elif ypos >= gridheight:
        grid.append(gridrow)
    return grid

def gridexpandx(grid,xpos):
    gridwidth = len(grid[0])
    gridheight = len(grid)
    if xpos < 0:
        for a in range(0,gridheight):
            grid[a].insert(0, '.')
    elif xpos >= gridwidth:
        for a in range(0,gridheight):
            grid[a].append('.')
    return grid

def xyfix(listy):
    if listy[0] < 0:
        listy[0] = 0
    if listy[1] < 0:
        listy[1] = 0
    return listy


input_text = 'daninput.txt'

nodes = newlinefile(input_text)
nodes = listoflists(nodes)

xpos = (len(nodes[0]) - 1) / 2
ypos = (len(nodes) - 1) / 2
facing = 'u'

burstcount = 0

for i in range(0,10000000):
    facing = turnme(nodes[ypos][xpos],facing)
    nodes[ypos][xpos] = infection(nodes[ypos][xpos])
    if nodes[ypos][xpos] == '#':
        burstcount += 1
    xy = movement(xpos,ypos,facing)
    nodes = gridexpandy(nodes,xy[1])
    nodes = gridexpandx(nodes,xy[0])
    xy = xyfix(xy)
    xpos = xy[0]
    ypos = xy[1]
    if i % 100000 == 0:
        print i

print "22b: " + str(burstcount)
