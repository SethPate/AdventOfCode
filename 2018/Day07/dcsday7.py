#dan day 7

worker_count = 5
base_time = 60
input_text = 'dcsday7input.txt'
current_time = 0

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

def get_letter_value(a,b):
    return ord(a) + b - 64

def make_new_workers(a):
    for number in range(a):
        Worker()

def make_holding_list(a,b,c):
    for item in a:
        if compare_lists(sequence_set[item].expanded_prereqs,b) == 0 and item not in b and item not in c:
            c.append(item)
            c.sort()
    return c

def make_holding_list_7b(a,b,c,d):
    for item in a:
        if compare_lists(sequence_set[item].expanded_prereqs,b) == 0 and item not in b and item not in c and item not in d:
            c.append(item)
            c.sort()
    return c

class Letter:
    def __init__(self,item):
        self.name = item
        self.prereqs = []
        self.expanded_prereqs = self.prereqs
        self.successors = []
        self.status = ''
        self.time_to_completion = -1
        self.worker = ''
    
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
        print self.worker
        print self.time_to_completion

class Worker:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.name = ''
        self.status = 'available'
        self.assignment = ''

instruction_list = newlinefile(input_text)
letters_list = get_all_letters(instruction_list)
sequence_set = lettermaker(letters_list,instruction_list)
sequenced_letters = []
holding_list = []

for item in letters_list:
    prereq_expansion(item)

while len(sequenced_letters) < len(letters_list):
    holding_list = make_holding_list(letters_list,sequenced_letters,holding_list)
    sequenced_letters.append(holding_list[0])
    holding_list.pop(0)

print("7a: " + conv_list_to_string(sequenced_letters))

#7b work

#how many workers do we have available?
make_new_workers(worker_count)

#how much time does each letter in the set require?
worktime_details = {}
sequenced_letters = []
work_queue = []
holding_list = []
needed_workers = 0

while len(sequenced_letters) < len(letters_list):
    for item in letters_list:
        holding_list = make_holding_list_7b(letters_list,sequenced_letters,holding_list,work_queue)
    needed_workers = len(holding_list) + len(work_queue)
    
    #determine how many workers are available. 
    available_workers = min(needed_workers,worker_count)
    
    #assign workers to items in the holding list.
    #once an item is assigned, remove it from the holding list.
    for a in range(0,available_workers):
        if Worker._registry[a].status == 'available' and len(holding_list) > 0:
            Worker._registry[a].status = 'busy'
            Worker._registry[a].assignment = holding_list[0]
            work_queue.append(holding_list[0])
            sequence_set[holding_list[0]].time_to_completion = get_letter_value(holding_list[0],base_time)
            sequence_set[holding_list[0]].worker = a
            holding_list.pop(0)
    
    newly_sequenced_letters = []
    
    #reduce everyone's time
    for item in work_queue:
        sequence_set[item].time_to_completion -= 1
    
    #check if any of the jobs have completed.
    #if so:
    ## add the completed item to a list, "newly_sequenced_letters."
    ## change the worker status to available and clear their current assignment.
    ## remove the worker from the sequence_set's position.
    ## clear the item from the work queue.
    for item in work_queue:
        if sequence_set[item].time_to_completion == 0:
            newly_sequenced_letters.append(sequence_set[item].name)
            Worker._registry[sequence_set[item].worker].status = 'available'
            Worker._registry[sequence_set[item].worker].assignment = ''
            sequence_set[item].worker = ''
            work_queue.remove(item)

    #check completed work
    newly_sequenced_letters.sort()
    
    #append recently-completed work to the existing list.
    if len(newly_sequenced_letters) > 0:
        sequenced_letters = merge_lists(sequenced_letters,newly_sequenced_letters)
    
    #increment time!
    current_time += 1    

print("7b: " + str(current_time))
