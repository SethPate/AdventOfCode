freq = 0

with open("2018/Day01/agd_input1.txt", "r") as x:
  data = x.readlines()

for i in range(len(data)):
  freq = freq + int(data[i])

print(freq)