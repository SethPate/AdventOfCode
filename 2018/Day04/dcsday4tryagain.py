#dan day 4, third attempt

from datetime import datetime
from datetime import timedelta

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split("\n")
    input1.remove('')
    return input1 

def sleep_log_fix(a):
    a.sort()
    for i in range(0,len(a)):
        c = a[i].find(' begins')
        if c > -1:
            guard_name = a[i][19:c]
        else:
            a[i] = a[i][0:19] + guard_name + " " + a[i][19:]
    return a

def sleep_entry_breakdown(a):
    b = a[19:]
    b = b.split(" ")
    c = []
    c.append(int(b[1][1:]))
    if b[2] == 'falls':
        c.append('asleep')
    else:
        c.append('awake')
    return c

def get_guards(a):
    c = []
    for item in a:
        b = item[19:]
        b = b.split(" ")
        if int(b[1][1:]) not in c:
            c.append(int(b[1][1:]))
    return c

def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

input_text = 'dcsday4input.txt'


sleep_log = newlinefile(input_text)

sleep_log = sleep_log_fix(sleep_log)

timestamp_dict = {}

start_time = datetime.strptime(sleep_log[0][1:17],"%Y-%m-%d %H:%M")
end_time = datetime.strptime(sleep_log[len(sleep_log) - 1][1:17],"%Y-%m-%d %H:%M")
current_time = start_time

while current_time <= end_time:
    timestamp_dict[current_time] = 0
    current_time += timedelta(minutes=1)
    
for i in range(0,len(sleep_log)):
    log_timestamp = datetime.strptime(sleep_log[i][1:17],"%Y-%m-%d %H:%M")
    timestamp_dict[log_timestamp] = sleep_entry_breakdown(sleep_log[i])
    
current_time = start_time

while current_time <= end_time:
    if timestamp_dict[current_time] == 0:
        timestamp_dict[current_time] = timestamp_dict[current_time - timedelta(minutes=1)]
    current_time += timedelta(minutes=1)

guard_dict = {}
guard_list = get_guards(sleep_log)

for item in guard_list:
    guard_dict[item] = 0

#get sleepiest guard
current_time = start_time

while current_time <= end_time:
    if timestamp_dict[current_time][1] == 'asleep' and current_time.hour == 0:
        guard_dict[timestamp_dict[current_time][0]] += 1
    current_time += timedelta(minutes=1)

guard_number = (keywithmaxval(guard_dict))

minutes_dict = {}
for i in range(0,60):
    minutes_dict[i] = 0

current_time = start_time

while current_time <= end_time:
    if timestamp_dict[current_time][0] == guard_number and timestamp_dict[current_time][1] == 'asleep' and current_time.hour == 0:
        minutes_dict[current_time.minute] += 1
    current_time += timedelta(minutes=1)

minute_number = (keywithmaxval(minutes_dict))

print("4a: " + str(guard_number * minute_number))

#4b
current_time = start_time
guard_min_dict = {}

while current_time <= end_time:
    if current_time.hour == 0 and timestamp_dict[current_time][1] == 'asleep':
        temp_gm_name = str(timestamp_dict[current_time][0]) + " " + str(current_time.minute)
        if temp_gm_name not in guard_min_dict:
            guard_min_dict[temp_gm_name] = 1
        else:
            guard_min_dict[temp_gm_name] += 1
    current_time += timedelta(minutes=1)

guard_min_solution = keywithmaxval(guard_min_dict)
guard_min_solution = guard_min_solution.split(' ')
print("4b: " + str(int(guard_min_solution[0])*int(guard_min_solution[1])))
