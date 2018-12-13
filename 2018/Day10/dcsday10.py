#dan day 10

import time

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    input1.remove('')
    return input1

def list_to_string(b):
    c = ''
    for d in range(0,len(b)):
        c = c + b[d]
    return c

def record_splitter(a):
    a = a.replace(" ","")
    a = a.replace("=<",":")
    a = a.replace(" ",":")
    a = a.replace(",",":")
    a = a.replace(">",":")
    a = a.split(":")
    return a

def get_size_of_grid_y(a):
    min_y = a[0].y_pos
    max_y = a[0].y_pos
    for item in a:
        if min_y < item.y_pos:
            mix_y = item.y_pos
        if max_y > item.y_pos:
            max_y = item.y_pos
    return max_y - min_y

def get_size_of_grid_x(a):
    min_x = a[0].x_pos
    max_x = a[0].x_pos
    for item in a:
        if min_x < item.x_pos:
            mix_x = item.x_pos
        if max_x > item.x_pos:
            max_x = item.x_pos
    return max_x - min_x

class Point():
    _registry = []
    
    def __init__(self,input_string):
        b = record_splitter(input_string)
        self._registry.append(self)
        self.x_pos = int(b[1])
        self.y_pos = int(b[2])
        self.x_pos_disp = int(b[1])
        self.y_pos_disp = int(b[2])
        self.x_vel = int(b[4])
        self.y_vel = int(b[5])
    
    def print_info(self):
        print self.x_pos
        print self.y_pos
        print self.x_vel
        print self.y_vel
    
    def moveit(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

input_text = 'dcsday10input.txt'

instructions = newlinefile(input_text)

for a in range(0,len(instructions)):
    Point(instructions[a])

current_min_x = 0
current_min_y = 0

time_counter = 0

while True:

    current_min_x = 0
    current_min_y = 0

    #first, figure out the mins.
    Point._registry[0].x_pos = current_min_x
    Point._registry[0].y_pos = current_min_y
    current_max_x = current_min_x
    current_max_y = current_min_y
    
    for a in range(1,len(instructions)):
        if Point._registry[a].x_pos < current_min_x:
            current_min_x = Point._registry[a].x_pos
        if Point._registry[a].y_pos < current_min_y:
            current_min_y = Point._registry[a].y_pos
        if Point._registry[a].x_pos > current_max_x:
            current_max_x = Point._registry[a].x_pos
        if Point._registry[a].y_pos > current_max_y:
            current_max_y = Point._registry[a].y_pos
    
    #second, adjust to a 0,0 basis.
    for a in range(0,len(instructions)):
        Point._registry[a].x_pos_disp = Point._registry[a].x_pos - current_min_x
        Point._registry[a].y_pos_disp = Point._registry[a].y_pos - current_min_y
        
    x_size = current_max_x - current_min_x
    y_size = current_max_y - current_min_y

    #third, create the display table
    if y_size < 150:
        display_table = []
        for i in range(0,y_size + 1):
            new_row = []
            for j in range(0,x_size + 1):
                new_row.append('.')
            display_table.append(new_row)
    
    #fourth, fill in the pound signs.
        for a in range(0,len(instructions)):
            display_table[Point._registry[a].y_pos_disp][Point._registry[a].x_pos_disp] = '#'
            
        for item in display_table:
            print list_to_string(item)
        time.sleep(5)
        print("\n")
        
    print time_counter
    time_counter += 1

    #finally, do the moves
    for a in range(0,len(instructions)):
        Point._registry[a].moveit()
    
