#DCS Day 9

def fileimport(input_file1):
    input1 = open(input_file1, 'r')
    input1 = input1.read()
    return input1

def listmaker(a):
    b = a.split()
    return b

class Heightmap:
    def __init__(self,a):
        self.input_list = a
        self.height_dict = {}
        self.low_points_score = 0
        self.low_points_list = []
        self.basin_dict = {}
        self.basin_dict_lengths = []

    def make_height_dict(self):
        for x in range(0,len(self.input_list)):
            for y in range(0,len(self.input_list[x])):
                self.height_dict['x' + str(x) + 'y' + str(y)] = int(input_list[x][y])

    def remove_process(self,my_list,x_val,y_val):
        b = 'x' + str(x_val) + 'y' + str(y_val)
        if b in my_list:
            my_list.remove(b)
        return my_list

    def make_basin_dict(self):
        for item in self.low_points_list:
            self.basin_dict[item] = []
            self.basin_dict[item].append(item)

    def make_check_list(self,x,y):
        my_list = []
        my_list.append('x' + str(x) + 'y' + str(y + 1))
        my_list.append('x' + str(x) + 'y' + str(y - 1))
        my_list.append('x' + str(x + 1) + 'y' + str(y))
        my_list.append('x' + str(x - 1) + 'y' + str(y))
        if x + 1 == len(self.input_list):
            my_list = self.remove_process(my_list,x + 1,y)
        if x - 1 < 0:
            my_list = self.remove_process(my_list,x - 1,y)
        if y + 1 == len(self.input_list[x]):
            my_list = self.remove_process(my_list,x,y + 1)
        if y - 1 < 0:
            my_list = self.remove_process(my_list,x,y - 1)
        return my_list

    def find_basin(self,basin_bottom):
        no_nines = 'no'
        search_list = list(basin_bottom)
        checked_list = []
        while no_nines == 'no':
            no_nines_this_time = 1
            for i in range(0,len(search_list)):
                check_list = []
                current_position = search_list[i].replace('x','')
                current_position = current_position.replace('y','|')
                current_pos_list = current_position.split('|')
                x = int(current_pos_list[0])
                y = int(current_pos_list[1])
                check_list = self.make_check_list(x,y)
                for item in check_list:
                    if self.height_dict[item] != 9 and item not in basin_bottom:
                        basin_bottom.append(item)
                        search_list.append(item)
                        no_nines_this_time = 0
                    checked_list.append(item)
            if no_nines_this_time == 1:
                no_nines = 'yes'

    def build_all_basins(self):
        for k in range(0,len(self.low_points_list)):
            self.find_basin(self.basin_dict[self.low_points_list[k]])
            self.basin_dict_lengths.append(len(self.basin_dict[self.low_points_list[k]]))
        self.basin_dict_lengths.sort(reverse = True)

    def get_low_points(self):
        low_points_total = 0
        for x in range(0,len(self.input_list)):
            for y in range(0,len(self.input_list[x])):
                check_list = self.make_check_list(x,y)
                low_point_status = 1
                for item in check_list:
                    if self.height_dict['x' + str(x) + 'y' + str(y)] >= self.height_dict[item]:
                        low_point_status = 0
                if low_point_status == 1:
                    self.low_points_list.append('x' + str(x) + 'y' + str(y))
                    self.low_points_score += self.height_dict['x' + str(x) + 'y' + str(y)] + 1

    def get_9a_solution(self):
        my_heightmap.make_height_dict()
        my_heightmap.get_low_points()
        return self.low_points_score

    def get_9b_solution(self):
        self.make_basin_dict()
        self.build_all_basins()
        return self.basin_dict_lengths[0] * self.basin_dict_lengths[1] * self.basin_dict_lengths[2]

data_input = fileimport('day9_input.txt')
input_list = listmaker(data_input)
my_heightmap = Heightmap(input_list)

print("9A: " + str(my_heightmap.get_9a_solution()))
print("9B: " + str(my_heightmap.get_9b_solution()))
