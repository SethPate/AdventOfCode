pline = []
ans_init = []
ans_next = []
with open("2018/Day02/agd_input2.txt", "r") as x:
    data = x.readlines()

for line in data:
    pline.append(line.split())

for i in range(len(pline)-1):
    let_init = list(str(pline[i]))
    let_init.pop()
    let_init.pop()
    let_init.pop(0)
    let_init.pop(0)
    for k in range(i+1,(len(pline)-1)):
        let_next = list(str(pline[k]))
        let_next.pop()
        let_next.pop()
        let_next.pop(0)
        let_next.pop(0)

        correct = 0
        for j in range (len(let_init)):
            if let_init[j] == let_next[j]:
                correct = correct + 1
        if correct == len(let_init)-1:
            ans_init = let_init
            ans_next = let_next


print(ans_init)
print(ans_next)
print(''.join(ans_init))

#     letters.sort()
#
#     for j in range(len(letters)):
#         for k in range(j+1,len(letters)):
#             if letters[k] != '0':
#                 if k+1 < len(letters):
#                     if letters[k] == letters[j]:
#                         if letters[k+1] == letters[j]:
#                             trip = 1
#                             letters[j] = '0'
#                             letters[j+1] = '0'
#                             letters[j+2] = '0'
#                         else:
#                             dup = 1
#                             letters[j] = '0'
#                             letters[j+1] = '0'
#                 elif k < len(letters):
#                     if letters[k] == letters[j]:
#                         dup = 1
#                         letters[j] = '0'
#                         letters[j+1] = '0'
#         print(letters)
#     totdup = totdup + dup
#     tottrip = tottrip + trip
#     dup = 0
#     trip = 0
#     print(totdup,tottrip,dup,trip)
#
# print(totdup)
# print(tottrip)
# print(totdup*tottrip)