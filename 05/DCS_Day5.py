#DCS Day 5

def fileimport(input_file1):
    input1 = open(input_file1, 'r')
    input1 = input1.read()
    return input1

def listmaker(a):
    b = a.split("\n")
    return b

def parse_input_list(a):
    b = []
    c = []
    for item in a:
        b.append(item.replace(' -> ',','))
    for item in b:
        c.append(item.split(','))
    return c

def build_diagram(a,b):
    dict_object = {}
    for i in range(0,a+1):
        for j in range(0,b+1):
            dict_object['x' + str(i) + 'y' + str(j)] = 0
    return dict_object

class Line:
    def __init__(self, a):
        self.full_name = ''
        self.x1 = int(a[0])
        self.y1 = int(a[1])
        self.x2 = int(a[2])
        self.y2 = int(a[3])
        self.direction = ''
        self.slope = ''
        self.line_length = ''
        self.x_direction = ''

    def get_direction(self):
        if self.x1 == self.x2:
            self.direction = 'horizontal'
        elif self.y1 == self.y2:
            self.direction = 'vertical'
        else:
            self.direction = 'diagonal'

    def get_max_x(self):
        if self.x1 > self.x2:
            return self.x1
        else:
            return self.x2

    def get_max_y(self):
        if self.y1 > self.y2:
            return self.y1
        else:
            return self.y2

    def handle_diagonal(self):
        self.slope = (self.y2 - self.y1) / (self.x2 - self.x1)
        if self.x2 > self.x1:
            self.x_direction = '+'
            self.line_length = self.x2 - self.x1 + 1
        else:
            self.x_direction = '-'
            self.line_length = self.x1 - self.x2 + 1
        


data_input = fileimport('day5_input_test.txt')
input_list = listmaker(data_input)

input_list = parse_input_list(input_list)

line_list = []

diagram_width = 0
diagram_length = 0
x_candidate = 0
y_candidate = 0

for i in range(0,len(input_list)):
    line_list.append(Line(input_list[i]))
    line_list[i].full_name = input_list[i]
    line_list[i].get_direction()
    if line_list[i].direction == 'diagonal':
        line_list[i].handle_diagonal()
    x_candidate = line_list[i].get_max_x()
    y_candidate = line_list[i].get_max_y()
    if x_candidate > diagram_length:
        diagram_length = x_candidate
    if y_candidate > diagram_width:
        diagram_width = y_candidate

#5A

diagram_dict = build_diagram(diagram_length, diagram_width)

for item in line_list:
    if item.direction == 'horizontal' and item.y1 > item.y2:
        for i in range(item.y2,item.y1 + 1):
            diagram_dict['x' + str(item.x1) + 'y' + str(i)] += 1
    elif item.direction == 'horizontal' and item.y2 > item.y1:
        for i in range(item.y1,item.y2 + 1):
            diagram_dict['x' + str(item.x1) + 'y' + str(i)] += 1
    elif item.direction == 'vertical' and item.x2 > item.x1:
        for i in range(item.x1,item.x2 + 1):
            diagram_dict['x' + str(i) + 'y' + str(item.y1)] += 1
    elif item.direction == 'vertical' and item.x1 > item.x2:
        for i in range(item.x2,item.x1 + 1):
            diagram_dict['x' + str(i) + 'y' + str(item.y1)] += 1


greater_than_one_count = 0

for i in range(0,diagram_length + 1):
    for j in range(0,diagram_width + 1):
        if diagram_dict['x' + str(i) + 'y' + str(j)] > 1:
            greater_than_one_count += 1

print("5A: " + str(greater_than_one_count))

#5B

for item in line_list:
    if item.direction == 'diagonal':
        if item.slope == 1 and item.x_direction == '+':
            for i in range(0,item.line_length):
                diagram_dict['x' + str(item.x1 + i) + 'y' + str(item.y1 + i)] += 1
        elif item.slope == 1 and item.x_direction == '-':
            for i in range(0,item.line_length):
                diagram_dict['x' + str(item.x1 - i) + 'y' + str(item.y1 - i)] += 1
        elif item.slope == -1 and item.x_direction == '+':
            for i in range(0,item.line_length):
                diagram_dict['x' + str(item.x1 + i) + 'y' + str(item.y1 - i)] += 1
        elif item.slope == -1 and item.x_direction == '-':
            for i in range(0,item.line_length):
                diagram_dict['x' + str(item.x1 - i) + 'y' + str(item.y1 + i)] += 1

greater_than_one_count = 0

for i in range(0,diagram_length + 1):
    for j in range(0,diagram_width + 1):
        if diagram_dict['x' + str(i) + 'y' + str(j)] > 1:
            greater_than_one_count += 1

print("5B: " + str(greater_than_one_count))
