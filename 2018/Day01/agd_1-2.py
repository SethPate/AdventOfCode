freq = 0
freqset = [freq]
repeat = 0
done = 0
with open("2018/Day01/agd_input1.txt", "r") as x:
  data = x.readlines()

while done == 0:
  for i in range(len(data)):
    freq = freq + int(data[i])
    if freq in freqset:
      repeat = freq
      done = 1
      break
    else:
      freqset.append(freq)


print(repeat)