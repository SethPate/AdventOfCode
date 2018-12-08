#dan day 7

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    input1.remove('')
    return input1

def get_all_letters(a):
    c = []
    for item in a:
        b = item.split(' ')
        if b[1] not in c:
            c.append(b[1])
        if b[7] not in c:
            c.append(b[7])
    return c

def lettermaker(a,b):
    my_dict = {}
    for item in a:
        my_dict[item] = Letter(item)
        my_dict[item].get_relationships(b)
        my_dict[item].great_sort()
    return my_dict

def compare_lists(a,b):
    c = 0
    for d in a:
        if d not in b:
            c += 1
    return c

def merge_lists(a,b):
    for c in b:
        if c not in a:
            a.append(c)
    return a

def remove_duplicates(a):
    b = []
    for item in a:
        if a not in b:
            b.append(item)
    return b

def prereq_expansion(a):
    b = sequence_set[a]
    d = 0
    while d < len(b.expanded_prereqs):
        c = sequence_set[b.expanded_prereqs[d]]
        b.expanded_prereqs = merge_lists(b.expanded_prereqs,c.expanded_prereqs)
        b.expanded_prereqs = remove_duplicates(b.expanded_prereqs)
        d += 1

def conv_list_to_string(a):
    c = ''
    for b in a:
        c = c + str(b)
    return c

def get_letter_value(a):
    return ord(a) - 4

class Letter:
    def __init__(self,item):
        self.name = item
        self.prereqs = []
        self.expanded_prereqs = self.prereqs
        self.successors = []
        self.status = ''
    
    def get_relationships(self,instructions):
        for item in instructions:
            item_list = item.split(' ')
            if item_list[7] == self.name:
                self.prereqs.append(item_list[1])
            if item_list[1] == self.name:
                self.successors.append(item_list[7])
    
    def great_sort(self):
        self.prereqs.sort()
        self.successors.sort()
    
    def print_details(self):
        print self.name
        print "prereqs: "
        print self.prereqs
        print "expanded prereqs: "
        print self.expanded_prereqs

input_text = 'dcsday7input.txt'

instruction_list = newlinefile(input_text)
letters_list = get_all_letters(instruction_list)
sequence_set = lettermaker(letters_list,instruction_list)
sequenced_letters = []
holding_list = []

for item in letters_list:
    prereq_expansion(item)

while len(sequenced_letters) < len(letters_list):
    for item in letters_list:
        if compare_lists(sequence_set[item].expanded_prereqs,sequenced_letters) == 0 and item not in sequenced_letters:
            if item not in holding_list:
                holding_list.append(item)
                holding_list.sort()
    sequenced_letters.append(holding_list[0])
    holding_list.pop(0)

print("5a: " + conv_list_to_string(sequenced_letters))

