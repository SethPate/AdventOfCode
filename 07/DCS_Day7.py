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

def get_distance(a,b,c):
    if c == '7A':
        return abs(a - b)
    elif c == '7B':
        c = 0
        d = abs(b - a)
        if d % 2 == 0:
            c = (d**2) / 2 + (0.5 * d)
        elif d % 2 == 1:
            c = ((d + 1)**2) / 2 + (0.5 * (d + 1)) - (d + 1)
        return c

class Crabs:
    def __init__(self,a,b):
        self.start_list = a
        self.min = a[0]
        self.max = a[-1]
        self.nav_dict = {}
        self.puzzle = b

    def find_fuel_usage(self):
        for i in range(0,self.max + 1):
            self.nav_dict[i] = 0
            for item in self.start_list:
                self.nav_dict[i] += get_distance(i,item,self.puzzle)
                
    def get_min_fuel(self):
        return min(self.nav_dict.values())


data_input = fileimport('day7_input.txt')
input_list = listmaker(data_input)

#7A

crab_set_7a = Crabs(input_list,'7A')
crab_set_7a.find_fuel_usage()
print("7A: " + str(crab_set_7a.get_min_fuel()))

#7B

crab_set_7b = Crabs(input_list,'7B')
crab_set_7b.find_fuel_usage()
print("7B: " + str(crab_set_7b.get_min_fuel()))
