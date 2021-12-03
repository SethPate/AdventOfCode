#DCS Day 1

def fileimport(input_file1):
	input1 = open(input_file1, 'r')
	input1 = input1.read()
	return input1

def listmaker(a):
	b = a.split("\n")
	b.remove("")
	return b

def get_depth_comparison(my_list):
    bigger_counter = 0
    for i in range(1,len(my_list)):
        if int(my_list[i - 1]) < int(my_list[i]):
            bigger_counter += 1
    return bigger_counter

data_input = fileimport('day1_input.txt')
input_list = listmaker(data_input)

#partA solution
print("Part A: " + str(get_depth_comparison(input_list)))

#partB solution
input_list_b = []

for i in range(2,len(input_list)):
    running_total = 0
    running_total += int(input_list[i - 2])
    running_total += int(input_list[i - 1])
    running_total += int(input_list[i])
    input_list_b.append(running_total)

print("Part B: " + str(get_depth_comparison(input_list_b)))
