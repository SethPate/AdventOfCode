#dan day 4

#take input, make into list.
def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split("\n")
    input1.remove('')
    return input1

def harmonize_delimiters(a):
    timestamp = a[1:17]
    a = a.replace('[','')
    a = a.replace(']','')
    a = a.replace('#','')
    a = a.replace('-',',')
    a = a.replace(' ',',')
    a = a.replace(':',',')
    b = a.split(',')
    b.insert(0,timestamp)
    return b

def conv_month_to_days(a):
    if a == 1:
        return 0
    elif a == 2:
        return 31
    elif a == 3:
        return 59
    elif a == 4:
        return 90
    elif a == 5:
        return 120
    elif a == 6:
        return 151
    elif a == 7:
        return 181
    elif a == 8:
        return 212
    elif a == 9:
        return 243
    elif a == 10:
        return 273
    elif a == 11:
        return 304
    elif a == 12:
        return 334

def create_timestamps(a):
    for item in a:
        timestamp_name = item
        timestamp_name = Timestamp(item)
        timestamp_name.timestamp_math()

def get_max_min(a):
    max_timestamp = max(a)
    min_timestamp = min(a)

class Timestamp:
    _registry = []

    def __init__(self,timelog_input):
        self._registry.append(self)
        self.name = timelog_input
        timelog_input = harmonize_delimiters(timelog_input)
        self.year = timelog_input[1]
        self.month = timelog_input[2]
        self.day = timelog_input[3]
        self.hour = timelog_input[4]
        self.minute = timelog_input[5]
        self.excel_time = 0
        self.sort_position = 0
        if timelog_input[6] == 'Guard':
            self.guard = timelog_input[7]
            self.awake_status = 'awake'
        elif timelog_input[6] == 'falls':
            self.guard = ''
            self.awake_status = 'asleep'
        else:
            self.guard = ''
            self.awake_status = 'awake'
        
    def timestamp_math(self):
        excel_day = float(conv_month_to_days(float(self.month)) + float(self.day) - 1)
        excel_hour = float(float(self.hour) / 24)
        excel_minute = float(float(self.minute) / 1440)
        self.excel_time = float(excel_day + excel_hour + excel_minute)
        
    
def timelog_sorter(a):
    b = []
    for item in Timestamp._registry:
        b.append(item.excel_time)
    b.sort()
    for item in Timestamp._registry:
        item.sort_position = b.index(item.excel_time)


input_text = 'dcsday4input.txt'


timelog = newlinefile(input_text)

#print(timelog)

create_timestamps(timelog)
timelog_sorter(Timestamp._registry)
    
#get max/min timestamps

max_excel_time = Timestamp._registry[0].excel_time
min_excel_time = Timestamp._registry[0].excel_time

for item in Timestamp._registry:
    if item.excel_time > max_excel_time:
        max_excel_time = item.excel_time
    if item.excel_time < min_excel_time:
        min_excel_time = item.excel_time

for i in range(0,len(Timestamp._registry)):
    if item.excel_time == min_excel_time:
        x = i
        break

print(Timestamp._registry[i].name)
print(Timestamp._registry[i].guard)

    
#print(max_excel_time)
#print(min_excel_time)
