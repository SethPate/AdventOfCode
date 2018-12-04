#dan day 3
#this was really clunky.

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split("\n")
    input1.remove('')
    return input1

def list_to_freq_table(a):
    freq_dict = {}
    for item in a:
        if item not in freq_dict:
            freq_dict[item] = 1
        else:
            freq_dict[item] += 1
    return freq_dict

class Gridsquare:
    h_pos = 0
    v_pos = 0
    holding = 'x'

class Instruction:
    fill_number = 0
    h_pos = 0
    v_pos = 0
    h_distance = 0
    v_distance = 0
    initial_size = 0
    updated_claim = 0
    
    def instruction_parse(self,input_text):
        space_one = input_text.find(" ")
        space_two = input_text.find(" ",space_one + 1)
        space_three = input_text.find(" ",space_two + 1)
        comma_loc = input_text.find(",")
        x_loc = input_text.find("x")
        self.fill_number = int(input_text[1:space_one])
        self.h_pos = int(input_text[space_two + 1:comma_loc])
        self.v_pos = int(input_text[comma_loc + 1:space_three - 1])
        self.h_distance = int(input_text[space_three + 1:x_loc])
        self.v_distance = int(input_text[x_loc + 1:])
        self.initial_size = self.h_distance * self.v_distance


input_text = 'dcsinputtext.txt'

instruction_input = newlinefile(input_text)

instruction_set = {}
instr_list = []

for item in instruction_input:
    instr_name = int(item[1:item.find(" ")])
    instruction_set[instr_name] = Instruction()
    instruction_set[instr_name].instruction_parse(item)
    instr_list.append(instr_name)

grid_square_set = {}
grid_square_dict = {}
counter = 0

for item in instr_list:
    for i in range(instruction_set[item].h_pos,instruction_set[item].h_pos + instruction_set[item].h_distance):
        for j in range(instruction_set[item].v_pos,instruction_set[item].v_pos + instruction_set[item].v_distance):
            grid_square_name = "h" + str(i) + "v" + str(j)
            if grid_square_name not in grid_square_dict:
                grid_square_dict[grid_square_name] = 0
                grid_square_set[grid_square_name] = Gridsquare()
                grid_square_set[grid_square_name].h_pos = i
                grid_square_set[grid_square_name].v_pos = j
                grid_square_set[grid_square_name].holding = instruction_set[item].fill_number
            else:
                if grid_square_set[grid_square_name].holding <> 'd':
                    grid_square_set[grid_square_name].holding = 'd'
                    counter += 1
                    
print("3a: " + str(counter))

#3b solution
area_list = []

for item in grid_square_dict:
    area_list.append(grid_square_set[item].holding)

grid_square_freq_table = list_to_freq_table(area_list)

for item in instr_list:
    if instruction_set[item].fill_number in grid_square_freq_table:
        instruction_set[item].updated_claim = grid_square_freq_table[item]
        if instruction_set[item].updated_claim == instruction_set[item].initial_size:
            print("3b: " + str(instruction_set[item].fill_number))
            break
