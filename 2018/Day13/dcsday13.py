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
        self.cart_number = 0
        self.direction = ''
        self.next_turn = 'L'
        self.x_coordinate = 0
        self.y_coordinate = 0
        self.prev_point = ''
        self.current_point = ''
    
    def assign_carts(self):
        self.current_point = 'x' + str(self.x_coordinate) + 'y' + str(self.y_coordinate)
        tracks[self.current_point].current_carts.append(self.cart_number)
    
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
        #track_point = tracks[self.prev_point]
        if tracks[self.prev_point].pos_type == '-':
            self.move_dash()
            #print "-"
        elif tracks[self.prev_point].pos_type == '|':
            self.move_pipe()
            #print "pipe"
        elif tracks[self.prev_point].pos_type == '/':
            self.move_fs()
            #print "fs"
        elif tracks[self.prev_point].pos_type == '\\':
            self.move_bs()
            #print "bs"
        elif tracks[self.prev_point].pos_type == '+':
            self.cart_turn()
            self.move_plus()
        self.current_point = 'x' + str(self.x_coordinate) + 'y' + str(self.y_coordinate)
        tracks[self.prev_point].current_carts.remove(self.cart_number)
        tracks[self.current_point].current_carts.append(self.cart_number)
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
        print("cart number: " + str(self.cart_number))
        print("direction: " + str(self.direction))
        print("next turn: " + str(self.next_turn))
    
    def check_current_point(self):
        #print tracks[self.current_point].current_carts
        #print self.x_coordinate
        #print self.y_coordinate
        #time.sleep(1)
        if len(tracks[self.current_point].current_carts) > 1:
            print "collision!"
            print self.current_point
            #crash_deletion(tracks[self.current_point].current_carts)
            #sys.exit()

#def crash_deletion(a):
    #for item in a:
        #Carts._registry.remove(item)

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
            #print b[point_name].pos_type
    return b

def run_turn():
    #print tracks['x4y2'].pos_type
    already_moved = {}
    for y in range(0,get_height(track_points)):
        for x in range(0,get_width(track_points)):
            point_name = "x" + str(x) + "y" + str(y)
            #print point_name
            if len(tracks[point_name].current_carts) > 0:
                #print point_name
                #print "cart number: " + str(tracks[point_name].current_carts[0])
                if Cart._registry[tracks[point_name].current_carts[0]] not in already_moved:
                    #print "run!"
                    #print Cart._registry[tracks[point_name].current_carts[0]].cart_number
                    already_moved[Cart._registry[tracks[point_name].current_carts[0]]] = 0
                    Cart._registry[tracks[point_name].current_carts[0]].cart_move()
    #print Cart._registry[0].current_point
    #print Cart._registry[0].direction
    #time.sleep(1)

#this function identifies the carts in the list of lists.
def get_carts():
    cart_signs = ['^','v','<','>']
    directions = [0,2,3,1]
    i = 0
    for item in Point._registry:
        if item.pos_type in cart_signs:
            Cart()
            Cart._registry[i].cart_number = i
            Cart._registry[i].x_coordinate = item.x_coordinate
            Cart._registry[i].y_coordinate = item.y_coordinate
            Cart._registry[i].direction = directions[cart_signs.index(item.pos_type)]
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

#Cart._registry[1].cart_info()

for item in Cart._registry:
    item.assign_carts()

while collision_constant >= 0:
    run_turn()
    
