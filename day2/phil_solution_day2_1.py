steps = []

infile = open('input_phil.txt', 'r')
for line in infile.readlines():
	for step in line.split(','):
		steps.append(step.strip())
infile.close()

pin = ''
keypad = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
x, y = 1, 1

for step in steps:
    for i in range(len(step.rstrip('\n'))):
        char = step[i]
        if char == 'U':
            y = max(0, y - 1)
        elif char == 'D':
            y = min(2, y + 1)
        elif char == 'L':
            x = max(0, x - 1)
        elif char == 'R':
            x = min(2, x + 1)
    pin  = pin + keypad[y][x]

print pin
