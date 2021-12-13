#DCS Day 11

def fileimport(input_file1):
    input1 = open(input_file1, 'r')
    input1 = input1.read()
    return input1

def listmaker(a):
    final_lol = []
    b = a.split('\n')
    for c in b:
        c_list = []
        c_list[:0] = c
        final_lol.append(c_list)
    return final_lol

class Octopus:
    def __init__(self,a,b,c):
        self.name = a
        self.x_pos = b
        self.y_pos = c
        self.energy_level = 0
        self.flash_step = 0
        self.flash_count = 0
        self.adjacent_octopodes = []
        
    def make_adjacent_list(self,z):
        self.adjacent_octopodes.append('x' + str(x) + 'y' + str(y + 1))
        self.adjacent_octopodes.append('x' + str(x) + 'y' + str(y - 1))
        self.adjacent_octopodes.append('x' + str(x + 1) + 'y' + str(y))
        self.adjacent_octopodes.append('x' + str(x - 1) + 'y' + str(y))
        self.adjacent_octopodes.append('x' + str(x + 1) + 'y' + str(y + 1))
        self.adjacent_octopodes.append('x' + str(x - 1) + 'y' + str(y - 1))
        self.adjacent_octopodes.append('x' + str(x + 1) + 'y' + str(y - 1))
        self.adjacent_octopodes.append('x' + str(x - 1) + 'y' + str(y + 1))
        if x + 1 == z:
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x + 1,y)
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x + 1,y + 1)
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x + 1,y - 1)
        if x - 1 < 0:
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x - 1,y)
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x - 1,y + 1)
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x - 1,y - 1)
        if y + 1 == z:
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x,y + 1)
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x - 1,y + 1)
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x + 1,y + 1)
        if y - 1 < 0:
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x,y - 1)
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x + 1,y - 1)
            self.adjacent_octopodes = self.remove_process(self.adjacent_octopodes,x - 1,y - 1)
    
    def remove_process(self,my_list,c,d):
        b = 'x' + str(c) + 'y' + str(d)
        if b in my_list:
            my_list.remove(b)
        return my_list

    def step_reset(self):
        self.flash_step = 0

class Flashdance:
    def __init__(self):
        self.energy_dict = {}

    def start_turn(self):
        for item in self.energy_dict:
            self.energy_dict[item] += 1

data_input = fileimport('day11_input.txt')
input_list = listmaker(data_input)
my_octopus_dict ={}
my_octopus_list = []

flashdance_list = []
flashdance_list.append(Flashdance())

for y in range(0,len(input_list)):
    for x in range(0,len(input_list[0])):
        o_name = 'x' + str(x) + 'y' + str(y)
        my_octopus_dict[o_name] = Octopus(o_name,x,y)
        my_octopus_list.append(o_name)
        my_octopus_dict[o_name].energy_level = input_list[x][y]
        my_octopus_dict[o_name].make_adjacent_list(len(input_list))
        flashdance_list[0].energy_dict[o_name] = int(my_octopus_dict[o_name].energy_level)
        
last_loop_flash_count = 0
total_flash_count = 0

i = 0
while last_loop_flash_count != 100:
    i += 1
    last_loop_flash_count = 0    
    for item in my_octopus_list:
        my_octopus_dict[item].flash_step = 0
    flashdance_list.append(Flashdance)
    flashdance_list[i].energy_dict = flashdance_list[i - 1].energy_dict.copy()
    flashdance_list[i].start_turn(flashdance_list[i])
    while max(flashdance_list[i].energy_dict.values()) > 9:
        for item in my_octopus_dict:
            if flashdance_list[i].energy_dict[item] > 9:
                if my_octopus_dict[item].flash_step == 0:
                    my_octopus_dict[item].flash_count += 1
                    last_loop_flash_count += 1
                    my_octopus_dict[item].flash_step = 1
                    flashdance_list[i].energy_dict[item] = 0
                for item2 in my_octopus_dict[item].adjacent_octopodes:
                    if my_octopus_dict[item2].flash_step == 0:
                        flashdance_list[i].energy_dict[item2] += 1
    if i == 100:
       for item in my_octopus_list:
           total_flash_count += int(my_octopus_dict[item].flash_count) 


print("11A: " + str(total_flash_count))
print("11B: " + str(i))
