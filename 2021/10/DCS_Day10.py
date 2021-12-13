#DCS Day 9

def fileimport(input_file1):
    input1 = open(input_file1, 'r')
    input1 = input1.read()
    return input1

def listmaker(a):
    b = a.split()
    return b

def score_errors(a):
    if a == ')':
        return 3
    elif a == ']':
        return 57
    elif a == '}':
        return 1197
    elif a == '>':
        return 25137
    else:
        return 0

class Errors:

    def __init__(self,a):
        self.subsystem_string = a
        self.subsystem_list = []
        self.completion_list = []
        self.left_facing = ['(','[','{','<']
        self.right_facing = [')','}',']','>']
        self.list_status = 'incomplete'
        self.completion_score = 0

    def clean_list(self):
        self.subsystem_list = []
        self.subsystem_list[:0] = self.subsystem_string
        #Precautionary 10A work to handle lists that were complete.
        #But all lists are incomplete so I commented them out.
        #self.subsystem_list.append('[')
        #self.subsystem_list.append('[')
        adjustment_counter = 1
        while adjustment_counter > 0:
            adjustment_counter = 1
            for i in range(0,len(self.subsystem_list) - 1):
                if self.subsystem_list[i] == '[' and self.subsystem_list[i+1] == ']':
                    self.subsystem_list[i] = '0'
                    self.subsystem_list[i + 1] = '0'
                    adjustment_counter += 1
                elif self.subsystem_list[i] == '(' and self.subsystem_list[i+1] == ')':
                    self.subsystem_list[i] = '0'
                    self.subsystem_list[i + 1] = '0'
                    adjustment_counter += 1
                elif self.subsystem_list[i] == '{' and self.subsystem_list[i+1] == '}':
                    self.subsystem_list[i] = '0'
                    self.subsystem_list[i + 1] = '0'
                    adjustment_counter += 1
                elif self.subsystem_list[i] == '<' and self.subsystem_list[i+1] == '>':
                    self.subsystem_list[i] = '0'
                    self.subsystem_list[i + 1] = '0'
                    adjustment_counter += 1
            adjustment_counter -= 1
            self.subsystem_list = [i for i in self.subsystem_list if i != '0']

    def get_first_error(self):
        for item in self.subsystem_list:
            if item in self.right_facing:
                self.list_status = 'errored'
                return item

    def build_completion_list(self):
        self.completion_list = self.subsystem_list[::-1]

    def score_remaining_list(self):
        for item in self.completion_list:
            self.completion_score *= 5
            if item == '(':
                self.completion_score += 1
            elif item == '[':
                self.completion_score += 2
            elif item == '{':
                self.completion_score += 3
            elif item == '<':
                self.completion_score += 4

def get_list_median(a):
    return ( (len(a) - 1) / 2)
   
data_input = fileimport('day10_input.txt')
input_list = listmaker(data_input)

error_list = []
for item in input_list:
    error_list.append(Errors(item))
    
#10A
    
score_10a = 0

for item in error_list:
    item.clean_list()
    my_error = (item.get_first_error())
    score_10a += score_errors(my_error)

print("10A: " + str(score_10a))

#10B

completion_scores_list = []

for item in error_list:
    if item.list_status == 'incomplete':
        item.build_completion_list()
        item.score_remaining_list()
        completion_scores_list.append(item.completion_score)

completion_scores_list.sort()

score_10b = completion_scores_list[int(get_list_median(completion_scores_list))]

print("10B: " + str(score_10b))
