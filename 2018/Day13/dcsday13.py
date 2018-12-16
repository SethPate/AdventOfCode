import time
import sys

#dan day 13

#notes on directions:
#0 = NORTH
#1 = EAST
#2 = SOUTH
#3 = WEST

#get the file, make it a list of lists.
def fileimport(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    input1.remove('')
    input2 = []
    for line in input1:
        list2 = list(line)
        input2.append(list2)
    return input2

#cart class to store information about individual carts.
#includes a function to turn based on turn rules.
#also includes a function to display info on the cart.
class Cart:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.cart_designator = 0
        self.direction = ''
        self.next_turn = 'L'
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.prev_point = ''
        self.current_point = ''
    
    def assign_carts(self):
        self.current_point = 'x' + str(self.x_coordinate) + 'y' + str(self.y_coordinate)
        tracks[self.current_point].current_carts.append(self.cart_designator)
    
    def cart_turn(self):
        if self.next_turn == 'L':
            #print 'I ran cart turn for some reason'
            self.direction -= 1
            self.next_turn = 'S'
            if self.direction == -1:
                self.direction = 3
        elif self.next_turn == 'S':
            #print "self.next_turn is S now"
            self.next_turn = 'R'
        elif self.next_turn == 'R':
            self.direction += 1
            self.next_turn = 'L'
            if self.direction == 4:
                self.direction = 0
    
    def cart_move(self):
        self.prev_point = self.current_point
        if tracks[self.prev_point].pos_type == '-':
            self.move_dash()
        elif tracks[self.prev_point].pos_type == '|':
            self.move_pipe()
        elif tracks[self.prev_point].pos_type == '/':
            self.move_fs()
        elif tracks[self.prev_point].pos_type == '\\':
            self.move_bs()
        elif tracks[self.prev_point].pos_type == '+':
            self.cart_turn()
            self.move_plus()
        self.current_point = 'x' + str(self.x_coordinate) + 'y' + str(self.y_coordinate)
        tracks[self.prev_point].current_carts.remove(self.cart_designator)
        tracks[self.current_point].current_carts.append(self.cart_designator)
        self.check_current_point()
    
    def move_dash(self):
        if self.direction == 1:
            self.x_coordinate += 1
        elif self.direction == 3:
            self.x_coordinate -= 1
        else:
            print "error"
            print self.prev_point
   
    def move_pipe(self):
        if self.direction == 0:
            self.y_coordinate -= 1
        elif self.direction == 2:
            self.y_coordinate += 1
        else:
            print "error"
            print self.prev_point
    
    def move_bs(self):
        if self.direction == 0:
            self.direction = 3
            self.x_coordinate -= 1
        elif self.direction == 1:
            self.direction = 2
            self.y_coordinate += 1
        elif self.direction == 2:
            self.direction = 1
            self.x_coordinate += 1
        elif self.direction == 3:
            self.direction = 0
            self.y_coordinate -= 1
        else:
            print "error"
            print self.prev_point
    
    def move_fs(self):
        if self.direction == 0:
            self.direction = 1
            self.x_coordinate += 1
        elif self.direction == 1:
            self.direction = 0
            self.y_coordinate -= 1
        elif self.direction == 2:
            self.direction = 3
            self.x_coordinate -= 1
        elif self.direction == 3:
            self.direction = 2
            self.y_coordinate += 1
        else:
            print "error"
            print self.prev_point
    
    def move_plus(self):
        if self.direction == 0:
            self.y_coordinate -= 1
        elif self.direction == 1:
            self.x_coordinate += 1
        elif self.direction == 2:
            self.y_coordinate += 1
        elif self.direction == 3:
            self.x_coordinate -= 1
        else:
            print "error"
            print self.prev_point
        
    def cart_info(self):
        print("x: " + str(self.x_coordinate))
        print("y: " + str(self.y_coordinate))
        print("cart number: " + str(self.cart_designator))
        print("direction: " + str(self.direction))
        print("next turn: " + str(self.next_turn))
    
    def check_current_point(self):
        if len(tracks[self.current_point].current_carts) > 1:
            print "collision!"
            print self.current_point
            crash_deletion(tracks[self.current_point].current_carts)
            tracks[self.current_point].current_carts = []
            #sys.exit()

def crash_deletion(a):
    for item in a:
        del cart_set[item]

def get_remaining_key(a):
    k=list(a.keys())
    return k[0]

#every point in our initial diagram is stored in a class.
#fix_tracks figures out what type of track lies below carts.
class Point:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.pos_type = ''
        self.current_carts = []
    
    def fix_tracks(self):
        if self.pos_type == '^' or self.pos_type == 'v':
            self.pos_type = '|'
        elif self.pos_type == '<' or self.pos_type == '>':
            self.pos_type = '-'
   
#these three functions are to take the list of lists and put each item into the Point class.
def get_width(a):
    return len(a[0])

def get_height(a):
    return len(a)

def make_points(a):
    b = {}
    for y in range(0,get_height(a)):
        for x in range(0,get_width(a)):
            point_name = "x" + str(x) + "y" + str(y)
            b[point_name] = Point()
            b[point_name].x_coordinate = x
            b[point_name].y_coordinate = y
            b[point_name].pos_type = a[y][x]
    return b

def run_turn():
    already_moved = {}
    for y in range(0,get_height(track_points)):
        for x in range(0,get_width(track_points)):
            point_name = "x" + str(x) + "y" + str(y)
            if len(tracks[point_name].current_carts) > 0:
                if cart_set[tracks[point_name].current_carts[0]] not in already_moved:
                    already_moved[cart_set[tracks[point_name].current_carts[0]]] = 0
                    cart_set[tracks[point_name].current_carts[0]].cart_move()
                    
cart_set = {}

#this function identifies the carts in the list of lists.
def get_carts():
    cart_signs = ['^','v','<','>']
    directions = [0,2,3,1]
    i = 0
    for item in Point._registry:
        if item.pos_type in cart_signs:
            cart_set[i] = Cart()
            cart_set[i].cart_designator = i
            cart_set[i].x_coordinate = item.x_coordinate
            cart_set[i].y_coordinate = item.y_coordinate
            cart_set[i].direction = directions[cart_signs.index(item.pos_type)]
            i += 1

input_text = 'dcsday13input.txt'
track_points = fileimport(input_text)
collision_constant = 0

tracks = {}
tracks = make_points(track_points)

already_moved = {}

get_carts()

for item in Point._registry:
    item.fix_tracks()

for item in Cart._registry:
    item.assign_carts()

#while collision_constant >= 0:
    #run_turn()

while len(cart_set) > 1:
    run_turn()
    
final_key = get_remaining_key(cart_set)

print cart_set[final_key].current_point
