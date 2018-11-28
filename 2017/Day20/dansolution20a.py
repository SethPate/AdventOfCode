#dansolution20

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split('\n')
    if '' in input1:
        input1.remove('')
    return input1

class Particle:
    name = 0
    x_pos = 0
    y_pos = 0
    z_pos = 0
    x_acc = 0
    y_acc = 0
    z_acc = 0
    x_vel = 0
    y_vel = 0
    z_vel = 0
    m_dist = 0
    avg_m_dist = 0

    def particlefacts(self):
        return '''This is particle %s.
        My position is %s, %s, %s.
        My acceleration is %s, %s, %s.
        My velocity is %s, %s, %s.
        My Manhattan distance is %s.''' % (self.name,
        self.x_pos, self.y_pos, self.z_pos,
        self.x_acc, self.y_acc, self.z_acc,
        self.x_vel, self.y_vel, self.z_vel,
        self.m_dist)

    def particle_init(self,instruction):
        for item in instruction:
            numlist = getnumbers(item)
            if item[0] == 'p':
                self.x_pos = numlist[0]
                self.y_pos = numlist[1]
                self.z_pos = numlist[2]
            elif item[0] == 'a':
                self.x_acc = numlist[0]
                self.y_acc = numlist[1]
                self.z_acc = numlist[2]
            elif item[0] == 'v':
                self.x_vel = numlist[0]
                self.y_vel = numlist[1]
                self.z_vel = numlist[2]
            else:
                print "ERROR"
                break

    def m_dist_calc(self):
        self.m_dist = abs(self.x_pos) + abs(self.y_pos) + abs(self.z_pos)

    def particle_update(self):
        self.prev_m_dist = self.m_dist
        self.x_vel += self.x_acc
        self.y_vel += self.y_acc
        self.z_vel += self.z_acc
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel
        self.z_pos += self.z_vel

    def avg_m_dist_calc(self):
        if iter_count == 1:
            self.avg_m_dist = self.m_dist
        else:
            self.avg_m_dist = (self.avg_m_dist * (iter_count - 1) + self.m_dist) / iter_count

def getnumbers(mystring):
    newlist = []
    newlist = mystring.split(',')
    startpoint = newlist[0].index('<') + 1
    endpoint = newlist[2].index('>')
    newlist[0] = int(newlist[0][startpoint:])
    newlist[1] = int(newlist[1])
    newlist[2] = int(newlist[2][:endpoint])
    return newlist

input_text = 'daninput.txt'

particle_dict = {}
particle_list = []

p_instructions = newlinefile(input_text)

for i in range(0,len(p_instructions)):
    p_instruction = p_instructions[i].split(', ')
    particle_dict[i] = Particle()
    particle_dict[i].name = i
    particle_dict[i].particle_init(p_instruction)

iter_count = 0

while iter_count < 1000:
    iter_count += 1
    for i in range(0,len(particle_dict)):
        particle_dict[i].particle_update()
        particle_dict[i].m_dist_calc()
        particle_dict[i].avg_m_dist_calc()

min_avg = particle_dict[0].avg_m_dist
min_particle = 0

for i in range(1,len(particle_dict)):
    if particle_dict[i].avg_m_dist < min_avg:
        min_avg = particle_dict[i].avg_m_dist
        min_particle = i

print "20a: " + str(min_particle)
