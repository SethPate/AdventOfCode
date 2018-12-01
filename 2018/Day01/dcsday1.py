#dan day1 puzzle

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split("\n")
    input1.remove('')
    return input1

def list_running_total(a):
    b = 0
    for item in a:
        b += int(item)
        #print b
    return int(b)

def duplicate_freq_check(a,b):
    if int(b) in a:
        return 1
    else:
        return 0

textimport = 'dcsday1input.txt'

frequency_list = newlinefile(textimport)

#print(frequency_list)

#1a process: quite simple. create a running total of all the list items.
final_total = list_running_total(frequency_list)
print("1a: " + str(final_total))

#1b process: more complex.

current_frequency = 0
dup_check = 0
loop_frequency_list = []

while dup_check == 0:
    for item in frequency_list:
        current_frequency += int(item)
        dup_check = duplicate_freq_check(loop_frequency_list,current_frequency)
        if dup_check == 1:
            print("1b: " + str(current_frequency))
            break
        else:
            loop_frequency_list.append(int(current_frequency))