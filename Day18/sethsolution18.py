f = open('sethinput.txt','r')
data = f.readlines()

instructions = {} #store all instructions here

for i in range(len(data)):
    instructions[i] = data[i].strip()
    
registers = {} #store all registers here

for i in instructions:
    registers[instructions[i][4]] = 0
    
lastSound = 0

position = 0

while position in instructions: #this is probably too complicated, but it works
    print(position)
    ins = instructions[position].split(' ')
    print('a is', registers)
    command = ins[0]
    x = ins[1]
    print('x is', x)
    if len(ins) == 3:
        if not ins[2].isalpha():
            y = int(ins[2])
        else:
            y = registers[ins[2]]
    print('y is', y)
    print(command,x,y)
    if command == 'snd': #play a sound
        lastSound = registers[x]
        position += 1
    elif command == 'set': #set a register to a value
        registers[x] = y
        position += 1
    elif command == 'add': #increase a register by a value
        registers[x] += y
        position += 1
    elif command == 'mul': #multiply a register by a value
        registers[x] *= y
        position += 1
    elif command == 'mod': #change a register to remainder division by a value
        registers[x] %= y
        position += 1
    elif command == 'rcv': #return the last sound played, and (in part A) break
        if registers[x] != 0: 
            print('last sound played was', lastSound)
            break
        else:
            print('no sound recovered because X = 0')
            position += 1
    elif command == 'jgz':
        if registers[x] > 0:
            position += y
        else:
            position += 1