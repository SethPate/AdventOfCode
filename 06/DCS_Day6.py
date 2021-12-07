#DCS Day 6

def fileimport(input_file1):
    input1 = open(input_file1, 'r')
    input1 = input1.read()
    return input1

def listmaker(a):
    b = a.split(",")
    return b

class Timer:
    def __init__(self):
        self.timer_list = list([0,0,0,0,0,0,0,0,0])
        self.reproducers = 0
        self.fish_count = 0

    def grow_day(self):
        self.reproducers = self.timer_list[0]
        self.timer_list.pop(0)
        self.timer_list.append(self.reproducers)
        self.timer_list[6] += self.reproducers

    def get_fish_count(self):
        for item in self.timer_list:
            self.fish_count += int(item)

data_input = fileimport('day6_input.txt')
input_list = listmaker(data_input)

#6A

my_timer = Timer()

for item in input_list:
    my_timer.timer_list[int(item)] += 1
    
for i in range(0,80):
    my_timer.grow_day()

my_timer.get_fish_count()

print("6A: " + str(my_timer.fish_count))

#6B

my_timer_6b = Timer()

for item in input_list:
    my_timer_6b.timer_list[int(item)] += 1

for i in range(0,256):
    my_timer_6b.grow_day()

my_timer_6b.get_fish_count()

print("6B: " + str(my_timer_6b.fish_count))
