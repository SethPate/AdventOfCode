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

def freq_repeat(a):
    dup_check = 0
    loop_frequency_dict = {}
    current_frequency = 0
    while True:
        for item in a:
            current_frequency += int(item)
            if current_frequency in loop_frequency_dict:
                return current_frequency
            else:
                loop_frequency_dict[current_frequency] = 0
    

textimport = 'dcsday1input.txt'

frequency_list = newlinefile(textimport)

#print(frequency_list)

#1a process: quite simple. create a running total of all the list items.
final_total = list_running_total(frequency_list)
print("1a: " + str(final_total))

#1b process: more complex.
print("1b: " + str(freq_repeat(frequency_list)))