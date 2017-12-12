#this doesn't work; don't use this.

from math import pi,sin,cos,fabs,sqrt

f = open('sethinput.txt', 'r')
directions = f.read()
#directions = 'n,nw'
print(directions)
directions = directions.split(',')
directions[-1] = directions[-1][:1]
print(directions)

x = 0 #track distance in the x
y = 0 #track distance in the y

ne = (pi/6)
n = (pi/2)
nw = (5*pi/6)
sw = (7*pi/6)
s = (3*pi/2)
se = (11*pi/6)

for direction in directions:
#    print(direction)
    if direction == 'ne':
        x += cos(ne)
        y += sin(ne)
    elif direction == 'n':
        x += cos(n)
        y += sin(n)
    elif direction == 'nw':
        x += cos(nw)
        y += sin(nw)
    elif direction == 'sw':
        x += cos(sw)
        y += sin(sw)
    elif direction == 's':
        x += cos(s)
        y += sin(s)
    elif direction == 'se':
        x += cos(se)
        y += sin(se)
    else:
        print('direction does not make sense')

hypotenuse = sqrt(x**2 + y**2)

print('answer to part a is', hypotenuse, 'round to', round(hypotenuse))