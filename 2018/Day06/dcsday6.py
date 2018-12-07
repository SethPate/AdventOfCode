#dan day 6

#1. Find the size of the grid.
#2. Create grid. Similar to timestamp problem--every space needs to be created.
#3. Grid characteristics: x_pos, y_pos, point_number, is_location, is infinite, is_shared, shared_list.
#4. Solve "is_infinite."
#5. Go through each item in grid Make infinite markers. Infinite = 0,y; x,0; max_x,0; 0, max_y.

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    input3 = []
    for item in input1:
        input2 = []
        if item is not '':
            item = item.split(',')
            b = int(item[0])
            c = int(item[1])
            input2.append(b)
            input2.append(c)
        if len(input2) > 1:
            input3.append(input2)
    return input3

def find_max_pos(a,b):
    current_max = a[0][b]
    for item in a:
        if item[b] > current_max:
            current_max = item[b]
    return current_max

def manhattan_distance(a,b,c,d):
    h_distance = abs(a-c)
    y_distance = abs(b-d)
    return h_distance + y_distance

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return listOfKeys

def keywithminvalue(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(min(v))]

def min_value_in_dict(dict_name):
    return min(dict_name, key = lambda x: dict_name.get(x) )

class Coordinate:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.name = ''
        self.point_number = 0
        self.x_pos = 0
        self.y_pos = 0
        self.is_location = 0
        self.is_infinite = 0
        self.is_shared = 0
        self.distance_from_point = 0
        self.shared_list = []
        self.all_distance_sum = 0
        
    def coordinate_info(self):
        print("name: " + str(self.name))
        print("point number: " + str(self.point_number))
        print("x_pos: " + str(self.x_pos))
        print("y_pos: " + str(self.y_pos))
        print("is location? " + str(self.is_location))
        print("distance from point: " + str(self.distance_from_point))
        
class Area:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.area = 0
        self.point_number = 0
        self.is_infinite = 0
    
input_text = 'dcsday6input.txt'

coordinate_list = newlinefile(input_text)

max_x = find_max_pos(coordinate_list,0)
max_y = find_max_pos(coordinate_list,1)

coordinate_set = {}
coordinate_names = []

#procedure to create all viable coordinates
for i in range(0,max_y + 1):
    for j in range(0,max_x + 1):
        coordinate_name = "x" + str(j) + "y" + str(i)
        coordinate_set[coordinate_name] = Coordinate()
        coordinate_set[coordinate_name].x_pos = j
        coordinate_set[coordinate_name].y_pos = i
        coordinate_names.append(coordinate_name)

#procedure to add point information to existing coordinates

point_names = []
point_numbers = []

point_numbers.append(-1)

a = 0
for item in coordinate_list:
    coordinate_name = "x" + str(item[0]) + "y" + str(item[1])
    coordinate_set[coordinate_name].point_number = a
    coordinate_set[coordinate_name].is_location = 1
    point_names.append(coordinate_name)
    point_numbers.append(a)
    a += 1

#fill in all of the fields about the coordinates
for item in coordinate_names:
    if item not in point_names:
        x1 = coordinate_set[item].x_pos
        y1 = coordinate_set[item].y_pos
        distance_checker = {}
        distance_list = []
        for item2 in point_names:
            x2 = coordinate_set[item2].x_pos
            y2 = coordinate_set[item2].y_pos
            distance_checker[coordinate_set[item2].point_number] = manhattan_distance(x1,y1,x2,y2)
            distance_list.append(manhattan_distance(x1,y1,x2,y2))
        min_value = min(distance_list)
        points_list = []
        points_list = getKeysByValue(distance_checker,min_value)
        coordinate_set[item].shared_list = points_list
        coordinate_set[item].distance_from_point = min_value
        if len(points_list) > 1:
            coordinate_set[item].point_number = -1
        else:
            coordinate_set[item].point_number = points_list[0]
        
#print coordinate_set["x7y7"].coordinate_info()

#create area by point number class
point_number_set = {}

for item in point_numbers:
    point_number_set[item] = Area()
    point_number_set[item].point_number = item

#get total size of areas
for item in coordinate_names:
    point_number_set[coordinate_set[item].point_number].area += 1


#exclude all point numbers with infinite bounds from consideration.
limited_point_numbers = list(point_numbers)

for item in coordinate_names:
    if coordinate_set[item].point_number in limited_point_numbers:
        if coordinate_set[item].x_pos == 0 or coordinate_set[item].x_pos == max_x:
            point_number_set[coordinate_set[item].point_number].is_infinite == 1
            limited_point_numbers.remove(coordinate_set[item].point_number)
        elif coordinate_set[item].y_pos == 0 or coordinate_set[item].y_pos == max_y:
            point_number_set[coordinate_set[item].point_number].is_infinite == 1
            limited_point_numbers.remove(coordinate_set[item].point_number)

max_area = 0

#print limited_point_numbers

for item in limited_point_numbers:
    if point_number_set[item].is_infinite == 0 and point_number_set[item].area > max_area:
        max_area = point_number_set[item].area

print("6a:" + str(max_area))

#6b

point_counter = 0

for item in coordinate_names:
    new_distance_sum = 0
    x1 = coordinate_set[item].x_pos
    y1 = coordinate_set[item].y_pos
    for item2 in point_names:
        x2 = coordinate_set[item2].x_pos
        y2 = coordinate_set[item2].y_pos
        new_distance_sum += manhattan_distance(x1,y1,x2,y2)
    coordinate_set[item].all_distance_sum = new_distance_sum
    if new_distance_sum < 10000:
        point_counter += 1

print("6b: " + str(point_counter))
