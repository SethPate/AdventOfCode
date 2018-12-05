#dan day 5

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = list(input1)
    input1.remove('\n')
    return input1

def char_comp(a,b):
    e_score = 0
    if a == b:
        e_score += 1
    if a.upper() == b.upper():
        e_score += 1
    return e_score

def remake_string(a):
    b = ''
    for item in a:
        b = b + item
    return b

def polymerize(a):
    i = 0
    while i < len(a) - 1:
        #print(polymer)
        if char_comp(a[i],a[i + 1]) == 1:
            a.pop(i + 1)
            a.pop(i)
            i -= 1
        else:
            i += 1
    return a

def get_unit_type_list(a):
    b = []
    for item in a:
        if item.upper() not in b:
            b.append(item.upper())
    return b

def remove_units(a,b):
    c = []
    for item in a:
        if item.upper() not in b:
            c.append(item)
    return c

def reduced_list_trials(full_list,possible_reductions,polymer_len_1):
    updated_polymer = []
    for unit in possible_reductions:
        updated_polymer = remove_units(polymer,unit)
        updated_polymer = polymerize(updated_polymer)
        if len(updated_polymer) < polymer_len_1:
            polymer_len_1 = len(updated_polymer)
    return polymer_len_1

#5a
polymer = newlinefile('dcsday5input.txt')
polymer_5a = polymerize(polymer)
polymer_len = len(polymer_5a)
print("5a: " + str((polymer_len)))

#5b
unit_type_list = get_unit_type_list(polymer)
polymer_len = reduced_list_trials(polymer,unit_type_list,polymer_len)
print("5b: " + str((polymer_len)))
