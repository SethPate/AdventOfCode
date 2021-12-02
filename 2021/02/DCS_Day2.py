#DCS Day 2

def fileimport(input_file1):
	input1 = open(input_file1, 'r')
	input1 = input1.read()
	return input1

def listmaker(a):
	b = a.split("\n")
	b.remove("")
	return b

def list_of_lists_maker(a):
    b = []
    for item in a:
        b.append(item.split(" "))
    return b

class Positions:
    
    def __init__(self,a,b):
        self.depth = a
        self.horizontal_pos = b
    
    def move_position(self,a):
        if a[0] == 'forward':
            self.horizontal_pos += int(a[1])
        elif a[0] == 'up':
            self.depth -= int(a[1])
        elif a[0] == 'down':
            self.depth += int(a[1])

class Positions_2b:
    
    def __init__(self,a,b,c):
        self.depth = a
        self.horizontal_pos = b
        self.aim = c
    
    def move_position(self,a):
        if a[0] == 'forward':
            self.horizontal_pos += int(a[1])
            self.depth += (self.aim * int(a[1]))
        elif a[0] == 'up':
            self.aim -= int(a[1])
        elif a[0] == 'down':
            self.aim += int(a[1])

data_input = fileimport('day2_input.txt')
input_list = listmaker(data_input)

instructions = list_of_lists_maker(input_list)

#2A solution
position_list = []
position_list.append(Positions(0,0))
current_position = 0

for item in instructions:
    position_list.append(Positions(position_list[current_position].depth,position_list[current_position].horizontal_pos))
    position_list[current_position + 1].move_position(item)
    current_position += 1

print("2A: " + str(position_list[current_position].depth * position_list[current_position].horizontal_pos))

#2b solution
position_list_2b = []
position_list_2b.append(Positions_2b(0,0,0))
current_position = 0

for item in instructions:
    position_list_2b.append(Positions_2b(position_list_2b[current_position].depth,position_list_2b[current_position].horizontal_pos,position_list_2b[current_position].aim))
    position_list_2b[current_position + 1].move_position(item)
    current_position += 1
    
print("2B: " + str(position_list_2b[current_position].depth * position_list_2b[current_position].horizontal_pos))
