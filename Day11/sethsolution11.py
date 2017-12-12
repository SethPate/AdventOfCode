f = open('sethinput.txt', 'r')
data = f.read()
data = data.strip()
data = data.split(',')

class hex(object):
    locations = []
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self):
        return "Hex (%s, %s, %s)"%(self.x, self.y, self.z)
    
    def ne(self):
        self.x += 1
        self.z += -1
        
    def n(self):
        self.y += 1
        self.z += -1
    
    def nw(self):
        self.x += -1
        self.y += 1

    def sw(self):
        self.x += -1
        self.z += 1
        
    def s(self):
        self.y += -1
        self.z += 1
        
    def se(self):
        self.x += 1
        self.y += -1

    def distance(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        dz = abs(self.z - other.z)
        return (dx + dy + dz) / 2

mover = hex(0,0,0)
origin = hex(0,0,0)

distances = []

for direction in data:
    if direction == 'ne':
        mover.ne()
    elif direction == 'n':
        mover.n()
    elif direction == 'nw':
        mover.nw()
    elif direction == 'sw':
        mover.sw()
    elif direction == 's':
        mover.s()
    elif direction == 'se':
        mover.se()
    else:
        print('direction does not make sense')
    distances.append(origin.distance(mover))

print('part a answer is', origin.distance(mover))

print('part b answer is', max(distances))