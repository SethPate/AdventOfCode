#DCS Day 3

def fileimport(input_file1):
	input1 = open(input_file1, 'r')
	input1 = input1.read()
	return input1

def listmaker(a):
	b = a.split("\n")
	b.remove("")
	return b

def binary_to_decimal(a):
    binary_multiplier = 1
    decimal_value = 0
    for i in range(0,len(a)):
        decimal_value += (binary_multiplier * int(a[-1 * (i + 1)]))
        binary_multiplier *= 2
    return decimal_value

class Binary_Position:
    
    def __init__(self,a):
        self.left_to_right_position = a
        self.one_count = 0
        self.zero_count = 0
        self.most_common = ''
        self.least_common = ''
    
    def frequency_count(self,a):
        if a == '1':
            self.one_count += 1
        else:
            self.zero_count += 1

data_input = fileimport('day3_input.txt')
diagnostic_report = listmaker(data_input)

#3A Solution
binary_position_list = []

for item in diagnostic_report:
    for i in range(0,len(item)):
        if len(binary_position_list) - 1 < i:
            binary_position_list.append(Binary_Position(i))
        binary_position_list[i].frequency_count(item[i])
            
gamma_string = ''
epsilon_string = ''

for item in binary_position_list:
    if item.one_count > item.zero_count:
        gamma_string = gamma_string +  '1'
        epsilon_string = epsilon_string + '0'
    else:
        gamma_string = gamma_string + '0'
        epsilon_string = epsilon_string + '1'

gamma_value = binary_to_decimal(gamma_string)
epsilon_value = binary_to_decimal(epsilon_string)

print("3A: " + str(gamma_value * epsilon_value))

#3B solution

oxygen_list = list(diagnostic_report)
co_list = list(diagnostic_report)

oxygen_binary_position_list = []

current_position = 0

while len(oxygen_list) > 1:
    current_length = len(oxygen_list)
    new_oxygen_list = []
    for item in oxygen_list:
        oxygen_binary_position_list.append(Binary_Position(current_position))
        oxygen_binary_position_list[current_position].frequency_count(item[current_position])
    if oxygen_binary_position_list[current_position].one_count >= oxygen_binary_position_list[current_position].zero_count:
        for i in range(0,current_length):
            if oxygen_list[i][current_position] == '1':
                new_oxygen_list.append(oxygen_list[i])
    else:
        for i in range(0,current_length):
            if oxygen_list[i][current_position] == '0':
                new_oxygen_list.append(oxygen_list[i])
    oxygen_list = []
    oxygen_list = list(new_oxygen_list)
    current_position += 1

co_binary_position_list = []

current_position = 0

while len(co_list) > 1:
    current_length = len(co_list)
    new_co_list = []
    for item in co_list:
        co_binary_position_list.append(Binary_Position(current_position))
        co_binary_position_list[current_position].frequency_count(item[current_position])
    if co_binary_position_list[current_position].one_count >= co_binary_position_list[current_position].zero_count:
        for i in range(0,current_length):
            if co_list[i][current_position] == '0':
                new_co_list.append(co_list[i])
    else:
        for i in range(0,current_length):
            if co_list[i][current_position] == '1':
                new_co_list.append(co_list[i])
    co_list = []
    co_list = list(new_co_list)
    current_position += 1

oxygen_value = binary_to_decimal(oxygen_list[0])
co_value = binary_to_decimal(co_list[0])

print("3B: " + str(oxygen_value * co_value))
