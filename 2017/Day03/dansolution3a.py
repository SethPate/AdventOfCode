#dansolution3

inputtext = 361527

class SpiralPoint:
    name = '0'
    hdistance = 0
    vdistance = 0
    mdistance = 0

    def pointfacts(self):
        print '''This is point %s. I have an hdistance of %s,
        a vdistance of %s, and an mdistance of %s.''' % (self.name,
        self.hdistance, self.vdistance, self.mdistance)

    def movement(self,a):
        if a == 'n':
            self.vdistance += 1
        elif a == 's':
            self.vdistance -= 1
        elif a == 'e':
            self.hdistance += 1
        elif a == 'w':
            self.hdistance -= 1

    def mdistancecalc(self):
        return abs(self.hdistance) + abs(self.vdistance)

def turnme(a):
    if a == 'e':
        return 'n'
    elif a == 'n':
        return 'w'
    elif a == 'w':
        return 's'
    elif a == 's':
        return 'e'

#2a procedure
spiralpoint_dict = {}
maxe = 0
maxw = 0
maxn = 0
maxs = 0
direction = 'e'

spiralpoint_dict[1] = SpiralPoint()
spiralpoint_dict[1].name = 1

i = 2

while i <= inputtext:
    spiralpoint_dict[i] = SpiralPoint()
    spiralpoint_dict[i].name = i
    spiralpoint_dict[i].hdistance = spiralpoint_dict[i-1].hdistance
    spiralpoint_dict[i].vdistance = spiralpoint_dict[i-1].vdistance

    spiralpoint_dict[i].movement(direction)

    if direction == 'e' and abs(spiralpoint_dict[i].hdistance) > maxe:
        maxe = abs(spiralpoint_dict[i].hdistance)
        directionchange = 1

    if direction == 'n' and abs(spiralpoint_dict[i].vdistance) > maxn:
        maxn = abs(spiralpoint_dict[i].vdistance)
        directionchange = 1

    if direction == 'w' and abs(spiralpoint_dict[i].hdistance) > maxw:
        maxw = abs(spiralpoint_dict[i].hdistance)
        directionchange = 1

    if direction == 's' and abs(spiralpoint_dict[i].vdistance) > maxs:
        maxs = abs(spiralpoint_dict[i].vdistance)
        directionchange = 1

    if directionchange == 1:
        direction = turnme(direction)
        directionchange = 0

    spiralpoint_dict[i].mdistance = spiralpoint_dict[i].mdistancecalc()
    i += 1

print spiralpoint_dict[inputtext].pointfacts()
