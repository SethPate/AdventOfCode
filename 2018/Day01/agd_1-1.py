freq = 0

with open("input.txt", "r") as x:
  data = x.readlines()

for i in range(len(data)):
  freq = freq + int(data[i])

print(freq)