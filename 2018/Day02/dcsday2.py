#dan day2

#take input, make into list.
def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split("\n")
    input1.remove('')
    return input1

#convert a string into a list of single-character fields.
def string_to_list(a):
    c = []
    for b in range(0,len(a)):
        c.append(a[b])
    return c

#create frequency dictionary out of list.
def list_to_freq_table(a):
    freq_dict = {}
    for item in a:
        if item not in freq_dict:
            freq_dict[item] = 1
        else:
            freq_dict[item] += 1
    return freq_dict

#check how many values in dict a = b.
def dict_count(a,b):
    c = 0
    for item in a:
        if a[item] == b:
            c = 1
    return c

#get the Levenshtein distance between two strings of equal length--number of changes necessary to make equal.
def lev_distance(a,b):
    l_distance = 0
    for c in range(0,len(a)):
        if a[c] <> b[c]:
            l_distance += 1
    return l_distance

#return common characters from two strings of equal length.
def find_common_characters(a,b):
    d = ''
    for c in range(0,len(a)):
        if a[c] == b[c]:
            d = d + str(a[c])
    return d

#2a function - make freq table, count number of a's and number of b's, return product.
def checksum_calc(id_list,a,b):
    a_count = 0
    b_count = 0
    for package_id in id_list:
        id_string = string_to_list(package_id)
        id_table = list_to_freq_table(id_string)
        a_count += dict_count(id_table,a)
        b_count += dict_count(id_table,b)
    return a_count * b_count

#2b function - compare each set of strings, find two with an l_distance of exactly 1, return the common letters.
def string_match_comp(a):
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            l_distance_check = lev_distance(id_list[i],id_list[j])
            if l_distance_check == 1:
                match_1 = id_list[i]
                match_2 = id_list[j]
                return find_common_characters(match_1,match_2)

id_list = newlinefile("danday2input.txt")

#2a process
print("2a: " + str(checksum_calc(id_list,2,3)))

#2b process
print("2b: " + string_match_comp(id_list))
