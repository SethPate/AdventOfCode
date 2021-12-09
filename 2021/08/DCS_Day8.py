#DCS Day 8

def fileimport(input_file1):
	input1 = open(input_file1, 'r')
	input1 = input1.read()
	return input1

def listmaker(a):
	b = a.split("\n")
	b.remove("")
	return b

def make_list_of_lists(a):
    b = a.split(" ")
    return b

def check_length(a):
    if len(a) != 5 and len(a) != 6:
        return 1

class Entry:
    def __init__(self,a):
        self.segment_pattern = []
        self.entry_list = a
        self.middle_row_letter = ''
        self.bottom_left_letter = ''
        self.top_right_letter = ''
        self.top_left_letter = ''
        self.top_row_letter = ''
        self.bottom_right_letter = ''
            
    def build_signals(self,signal_number,position):
        listified_entry = []
        listified_entry[:0] = self.entry_list[position]
        for item in listified_entry:
            #print(item)
            if item not in self.segment_pattern[signal_number]:
                self.segment_pattern[signal_number].append(item)
    
    def build_signals_single(self,signal_number,character):
        if character not in self.segment_pattern[signal_number]:
            self.segment_pattern[signal_number].append(character)
        
    def step_1(self):
        for i in range(0,10):
            self.segment_pattern.append([])
        self.segment_pattern[8] = ['a','b','c','d','e','f','g']
        for i in range(0,10):
            if len(self.entry_list[i]) == 2:
                self.build_signals(0,i)
                self.build_signals(1,i)
                self.build_signals(3,i)
                self.build_signals(4,i)
                self.build_signals(7,i)
                self.build_signals(9,i)
            elif len(self.entry_list[i]) == 3:
                self.build_signals(0,i)
                self.build_signals(3,i)
                self.build_signals(7,i)
                self.build_signals(9,i)
            elif len(self.entry_list[i]) == 4:
                self.build_signals(4,i)
                self.build_signals(9,i)
        
    def step_2(self):
        for item in self.segment_pattern[0]:
            if item not in self.segment_pattern[1]:
                self.build_signals_single(2,item)
                self.build_signals_single(3,item)
                self.build_signals_single(5,item)
                self.build_signals_single(6,item)
                self.build_signals_single(7,item)
                self.build_signals_single(8,item)
                self.build_signals_single(9,item)
    
    def step_3(self):
        for item in self.segment_pattern[4]:
            if item not in self.segment_pattern[1]:
                self.build_signals_single(5,item)                
                self.build_signals_single(6,item)
                self.build_signals_single(8,item)
                self.build_signals_single(9,item)

    def step_4(self):
        for item in self.segment_pattern[8]:
            if item not in self.segment_pattern[9]:
                self.build_signals_single(0,item)
                self.build_signals_single(2,item)
                self.build_signals_single(6,item)
                
    def step_5(self):
        for item in self.segment_pattern[8]:
            if item not in self.segment_pattern[1]:
                self.build_signals_single(6,item)
    
    def step_6(self):
        complete = 0
        zero_match_counter = 0
        for i in range(0,10):
            listified_entry = []
            listified_entry[:0] = self.entry_list[i]
            if len(listified_entry) == 6:
                zero_match_counter = 0
                for item in listified_entry:
                    if item in self.segment_pattern[0]:
                        zero_match_counter += 1
                if zero_match_counter == 5 and complete == 0:
                    complete = 1
                    self.segment_pattern[0] = listified_entry
                    for item in self.segment_pattern[8]:
                        if item not in self.segment_pattern[0]:
                            self.middle_row_letter = item
    
    def step_7(self):
        self.build_signals_single(5,self.middle_row_letter)                
        self.build_signals_single(6,self.middle_row_letter)
        self.build_signals_single(3,self.middle_row_letter)
        self.build_signals_single(2,self.middle_row_letter)
        self.build_signals_single(9,self.middle_row_letter)

    def step_8(self):
        zero_match_counter = 0
        complete = 0
        for i in range(0,10):
            listified_entry = []
            listified_entry[:0] = self.entry_list[i]
            if len(listified_entry) == 6:
                zero_match_counter = 0
                for item in listified_entry:
                    if item in self.segment_pattern[9]:
                        zero_match_counter += 1
                if zero_match_counter == 5 and complete == 0:
                    complete = 1
                    self.segment_pattern[9] = listified_entry
                    for item in self.segment_pattern[8]:
                        if item not in self.segment_pattern[9]:
                            self.bottom_left_letter = item
                    
        
    def step_9(self):
        self.build_signals_single(2,self.middle_row_letter)                
        self.build_signals_single(6,self.middle_row_letter)

    def step_10(self):
        zero_match_counter = 0
        complete = 0
        for i in range(0,10):
            listified_entry = []
            listified_entry[:0] = self.entry_list[i]
            if len(listified_entry) == 6:
                zero_match_counter = 0
                for item in listified_entry:
                    if item in self.segment_pattern[6]:
                        zero_match_counter += 1
                if zero_match_counter == 5 and complete == 0:
                    complete = 1
                    self.segment_pattern[6] = listified_entry
                    for item in self.segment_pattern[8]:
                        if item not in self.segment_pattern[6]:
                            self.top_right_letter = item
    def step_11(self):
        self.build_signals_single(2,self.top_right_letter)                
        self.build_signals_single(3,self.top_right_letter)
        
    def step_12(self):
        self.segment_pattern[5] = list(self.segment_pattern[9])
        self.segment_pattern[5].remove(self.top_right_letter)
        self.segment_pattern[3] = list(self.segment_pattern[2])
        self.segment_pattern[3].remove(self.bottom_left_letter)
        for item in self.segment_pattern[1]:
            if item not in self.segment_pattern[3]:
                self.segment_pattern[3].append(item)

    def step_13(self):
        for item in self.segment_pattern:
            item.sort()
    
    def get_total(self,input_list):
        output_string = ''
        for j in range(0,4):
            listified_entry = []
            listified_entry[:0] = input_list[(j + 1) * -1]
            listified_entry.sort()
            for k in range(0, len(self.segment_pattern)):
                if listified_entry == self.segment_pattern[k]:
                    output_string = str(k) + output_string
        return int(output_string)

data_input = fileimport('day8_input.txt')
signal_set = listmaker(data_input)

#Really straightforward 8A.

signal_lol = []

for item in signal_set:
    temp_list = make_list_of_lists(item)
    signal_lol.append(temp_list)
    
result_8a = 0

for item in signal_lol:
    if check_length(item[-1]) == 1:
        result_8a += 1
    if check_length(item[-2]) == 1:
        result_8a += 1
    if check_length(item[-3]) == 1:
        result_8a += 1
    if check_length(item[-4]) == 1:
        result_8a += 1

print("8A: " + str(result_8a))

#omg 8B

output_total = 0
my_entry_list = []

for l in range(0,len(signal_lol)):
    my_entry_list.append(Entry(signal_lol[l]))
    my_entry_list[l].step_1()
    my_entry_list[l].step_2()
    my_entry_list[l].step_3()
    my_entry_list[l].step_4()
    my_entry_list[l].step_5()
    my_entry_list[l].step_6()
    my_entry_list[l].step_7()
    my_entry_list[l].step_8()
    my_entry_list[l].step_9()
    my_entry_list[l].step_10()
    my_entry_list[l].step_11()
    my_entry_list[l].step_12()
    my_entry_list[l].step_13()

    output_total += my_entry_list[l].get_total(signal_lol[l])

print("8B: " + str(output_total))
