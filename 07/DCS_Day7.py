#DCS Day 7

def fileimport(input_file1):
    input1 = open(input_file1, 'r')
    input1 = input1.read()
    return input1

def listmaker(a):
    b = a.split(",")
    c = []
    for item in b:
        c.append(int(item))
        c.sort()
    return c

def get_distance_7a(a,b):
    return abs(a - b)

def get_distance_7b(a,b):
    c = 0
    d = abs(b - a)
    if d % 2 == 0:
        c = (d**2) / 2 + (0.5 * d)
    elif d % 2 == 1:
        c = ((d + 1)**2) / 2 + (0.5 * (d + 1)) - (d + 1)
    return c

class Crabs:
    def __init__(self,a):
        self.start_list = a
        self.min = a[0]
        self.max = a[-1]
        self.count = len(a)
        self.range = self.max - self.min
        self.distance_7b = 0
        self.nav_dict = {}


data_input = fileimport('day7_input.txt')
input_list = listmaker(data_input)

crab_set = Crabs(input_list)

#7A

position_dict = {}

for i in range(0,crab_set.max + 1):
    position_dict[i] = 0
    for item in crab_set.start_list:
        position_dict[i] += get_distance_7a(item,i)

min_value = min(position_dict.values())

print("7A: " + str(min_value))

#7B

position_dict_7b = {}

for i in range(0,crab_set.max + 1):
    position_dict_7b[i] = 0
    for item in crab_set.start_list:
        position_dict_7b[i] += get_distance_7b(i,item)

min_value_7b = min(position_dict_7b.values())

print("7B: " + str(min_value_7b))
