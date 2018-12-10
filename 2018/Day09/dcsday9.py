#dan day 9

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split(' ')
    return input1

class Game:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.status = [0]
        self.current_marble = 0
        self.marble_in_play = 1
        self.current_player = 0
    
    def play_routine(self):
        sequence_length = len(self.status)
        insert_pos = (self.status.index(self.current_marble) + 1) % sequence_length + 1
        self.status.insert(insert_pos,self.marble_in_play)
        self.current_marble = self.marble_in_play
        
    def play_23(self):
        Player._registry[self.current_player].score += self.marble_in_play
        pos_to_remove = self.status.index(self.current_marble) - 7
        if pos_to_remove < 0:
            pos_to_remove = len(self.status) + pos_to_remove
        Player._registry[self.current_player].score += self.status[pos_to_remove]
        self.status.pop(pos_to_remove)
        if pos_to_remove >= len(self.status):
            self.current_marble = self.status[0]
        else:
            self.current_marble = self.status[pos_to_remove]
 
    def determine_play(self):
        if self.marble_in_play % 23 == 0:
            self.play_23()
        else:
            self.play_routine()
        if self.current_player == player_count - 1:
            self.current_player = 0
        else:
            self.current_player += 1
        self.marble_in_play += 1


class Player:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.number = ''
        self.score = 0

#basic setup stuff
input_text = 'dcsday9input.txt'
parameters = newlinefile(input_text)

player_count = int(parameters[0])
total_marbles = int(parameters[6])

Game()

for a in range(0,player_count):
    Player()

for a in range(0,total_marbles):
    Game._registry[0].determine_play()

max_score = Player._registry[0].score

for a in range(1,player_count):
    if Player._registry[a].score > max_score:
        max_score = Player._registry[a].score

print("9a: " + str(max_score))
