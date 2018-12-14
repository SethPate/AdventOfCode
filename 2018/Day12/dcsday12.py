#dan day 12

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    input1.remove('')
    return input1

def find_first_pound(a):
    k=list(a.keys())
    k.sort()
    j = 0
    m = 0
    while j == 0:
        if a[k[m]].tg_status == '#':
            j = 1
        else:
            m += 1
    return k[m]

def find_last_pound(a):
    k=list(a.keys())
    k.sort()
    j = 0
    for b in range(0,len(k)):
        if a[k[b]].tg_status == '#':
            m = b
    return k[m]

def expand_gen_list(a,b,c):
    for i in range(1,6):
        if (b - i) not in pot_set:
            pot_set[b - i] = Pot()
            pot_set[b - i].position = b - i
        if (c + i) not in pot_set:
            pot_set[c + i] = Pot()
            pot_set[c + i].position = c + i
        pot_set[b - i].tg_status = '.'
        pot_set[c + i].tg_status = '.'
    return pot_set

def get_initial_generation(a):
    input1 = a.split(": ")
    return input1[1]

def get_set(a,b):
    c = ''
    for d in range(b,b+5):
        c = c + a[d].tg_status
    #print c
    return c

class Pot:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.position = 0
        self.tg_status = '.'
        self.ng_status = ''
        
    def gen_advance(self):
        self.tg_status = self.ng_status
        self.ng_status = ''
        
class Generation:
    _registry = []
    
    def __init__(self,a):
        self._registry.append(self)
        self.gen_list = a
        self.gen_number = 0
        self.plant_count = 0
        
class Rule:
    _registry = []
    
    def __init__(self,a):
        self._registry.append(self)
        self.rule_input = a[0:5]
        self.rule_output = a[-1:]

class PlantPositions:
    _registry = []
    
    def __init__(self,a):
        self._registry.append(self)
        self.pp_sum = a
        self.gen_number = 0
        self.diff_from_prev_gen = 0
    
    def get_prev_gen_count(self):
        self.diff_from_prev_gen = self.pp_sum - PlantPositions._registry[self.gen_number - 1].pp_sum


PlantPositions(0)

input_text = 'dcsday12input.txt'

generation_input = newlinefile(input_text)

for i in range(1,len(generation_input)):
    Rule(generation_input[i])

Generation(generation_input[0])

pot_set = {}

initial_generation = get_initial_generation(generation_input[0])

for i in range(0,len(initial_generation)):
    pot_set[i] = Pot()
    pot_set[i].position = i
    pot_set[i].tg_status = initial_generation[i]

plant_position_sums = {}

linear_yet = 0
j = 1

while linear_yet == 0:    

    first_pound_pos = find_first_pound(pot_set)
    last_pound_pos = find_last_pound(pot_set)

    pot_set = expand_gen_list(pot_set,first_pound_pos,last_pound_pos)
        
    set_start = first_pound_pos - 4

    next_gen_list = []

    for i in range(set_start,last_pound_pos + 1):
        test_set = get_set(pot_set,i)
        for item in Rule._registry:
            if test_set == item.rule_input:
                pot_set[i + 2].ng_status = item.rule_output
    
    for i in range(set_start,last_pound_pos + 1):
        next_gen_list.append(pot_set[i].ng_status)

    Generation(next_gen_list)
    Generation._registry[j].gen_number = j
    
    for item in Pot._registry:
        item.gen_advance()

    position_sum = 0
    
    for item in Pot._registry:
        if item.tg_status == '#':
            position_sum += item.position
    
    PlantPositions(position_sum)
    PlantPositions._registry[j].gen_number = j
    PlantPositions._registry[j].get_prev_gen_count()
    
    if j == 20:
        print("12a: " + str(PlantPositions._registry[j].pp_sum))
    
    if PlantPositions._registry[j].diff_from_prev_gen == PlantPositions._registry[j - 1].diff_from_prev_gen:
        if PlantPositions._registry[j].diff_from_prev_gen == PlantPositions._registry[j - 2].diff_from_prev_gen:
            linear_yet = 1
        else:
            j += 1
    else:
        j += 1

pp_sum_50billion = PlantPositions._registry[j].pp_sum + ((50000000000 - j) * PlantPositions._registry[j].diff_from_prev_gen)

print("12b: " + str(pp_sum_50billion))
