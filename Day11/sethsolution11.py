from math import pi,sin,cos

f = open('sethinput.txt', 'r')
directions = f.read()
#directions = 'ne,ne,ne'
directions = directions.split(',')

x = 0 #track distance in the x
y = 0 #track distance in the y

ne = (pi/4)
n = (pi/2)
nw = (3*pi/4)
sw = (5*pi/4)
s = (3*pi/2)
se = (7*pi/2)

for direction in directions:
    print(direction)
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
        y += sin(s)
    else:
        print('direction does not make sense')
        
print('answer to part a is', round((x ** 2 + y ** 2) ** .5))