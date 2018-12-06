#dan day 4, attempt 2

#take input, make into list.
def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.replace('[','')
    input1 = input1.replace(']','')
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

def round_down(a):
    if round(a,0) > a:
        a = round(a,0) - 1
    else:
        a = round(a,0)
    return a

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
    
def conv_days_to_month(a):
    if a >= 0 and a < 31:
        return 1
    elif a >= 32 and a < 59:
        return 2
    elif a >= 60 and a < 90:
        return 3
    elif a >= 91 and a < 120:
        return 4
    elif a >= 121 and a < 151:
        return 5
    elif a >= 152 and a < 181:
        return 6
    elif a >= 182 and a < 212:
        return 7
    elif a >= 213 and a < 243:
        return 8
    elif a >= 244 and a < 273:
        return 9
    elif a >= 274 and a < 304:
        return 10
    elif a >= 305 and a < 334:
        return 11
    else:
        return 12

def timestamp_maths(a):
    b = a[0:16]
    b = b.replace(':',',')
    b = b.replace(' ',',')
    b = b.replace('-',',')
    b = b.split(',')
    a_day = float(conv_month_to_days(int(b[1])) + int(b[2]))
    a_hour = float(float(b[3])/24)
    a_minute = float(float(b[4])/1440)
    return float(a_day + a_hour + a_minute)


class Timestamp:
    _registry = []

    def __init__(self):
        self._registry.append(self)
        self.name = timelog_input
        timelog_input = harmonize_delimiters(timelog_input)
        self.year = timelog_input[1]
        self.month = timelog_input[2]
        self.day = timelog_input[3]
        self.hour = timelog_input[4]
        self.minute = timelog_input[5]
        self.excel_time = 0
        #self.sort_position = 0
        #if timelog_input[6] == 'Guard':
            #self.guard = timelog_input[7]
            #self.awake_status = 'awake'
        #elif timelog_input[6] == 'falls':
            #self.guard = ''
            #self.awake_status = 'asleep'
        #else:
            #self.guard = ''
            #self.awake_status = 'awake'
            
    def timestamp_math(self):
        excel_hour = float(float(self.hour) / 24)
        excel_minute = float(float(self.minute) / 1440)
        self.excel_time = float(self.excel_day + excel_hour + excel_minute)

class Instruction:
    _registry = []
    
    def __init(self):
        self._registry.append(self)
        self.name = timelog_input
        timelog_input = harmonize_delimiters(timelog_input)
        self.year = timelog_input[1]
        self.month = timelog_input[2]
        self.day = timelog_input[3]
        self.hour = timelog_input[4]
        self.minute = timelog_input[5]
        self.excel_time = 0
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
        self.excel_time = float(self.excel_day + excel_hour + excel_minute)


#1. Figure out the earliest and last possible date in the range.

input_text = 'dcsday4input.txt'
timelog = newlinefile(input_text)

min_time = timestamp_maths(timelog[0])
max_time = min_time
min_pos = 0
max_pos = 0

for i in range(1,len(timelog)):
    if timestamp_maths(timelog[i]) < min_time:
        min_time = timestamp_maths(timelog[i])
        min_pos = i
    if timestamp_maths(timelog[i]) > max_time:
        max_time = timestamp_maths(timelog[i])
        max_pos = i

earliest_day = int(round_down(min_time))
latest_day = int(round_down(max_time))

print earliest_day
print latest_day

for item in timelog:
    timestamp_name = item
    timestamp_name = Instruction(item)
    timestamp_name.timestamp_math()

x = 0
for i in range(earliest_day,latest_day + 1):
    for j in range(0,61):
        Timestamp()
        Timestamp._registry[x].excel_day = i
        Timestamp._registry[x].hour = 0
        Timestamp._registry[x].minute = j
        Timestamp._registry[x].month = conv_days_to_month(Timestamp._registry[x].excel_day)
        Timestamp._registry[x].day = Timestamp._registry[x].excel_day - conv_month_to_days(Timestamp._registry[x].month)
        Timestamp._registry[x].timestamp_math()
        x += 1

for i in range(0,x):
    for j in range(0,len(Instruction._registry)):
        
