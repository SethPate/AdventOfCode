#dansolution17
def getnewposition(base_list,current_position,rate):
    movetotal = rate % len(base_list)
    new_position = (current_position + movetotal) % len(base_list) + 1
    return new_position

def getnewpos17b(length_of_list,current_position,rate):
    movetotal = rate % length_of_list
    new_position = (current_position + movetotal) % length_of_list + 1
    return new_position

spinlockrate = 354
#spinlockrate = 3

#17a solution
spin_list = [0]
location = 0

for i in range(1,2018):
    location = getnewposition(spin_list,location,spinlockrate)
    spin_list.insert(location,i)

loc2017 = spin_list.index(2017)
print "17a: " + str(spin_list[loc2017 + 1])

#17b solution

spin_list = [0]
location = 0
cur_pos = 0
maxi = 0

#instead of building a list, we're going to simulate it based on an assumed length.
#every time the position is 1, we're going to store the insertion in "maxi."
#after 50,000,000 runs, we'll know the highest value in that first position.
#the first position always borders zero. that's the only way this works.
for i in range(1,50000001):
    location = getnewpos17b(i,cur_pos,spinlockrate)
    cur_pos = location
    if cur_pos == 1:
        maxi = i

print "17b: " + str(maxi)
