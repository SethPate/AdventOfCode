#dan day 9

def newlinefile(a):
    input1 = open(a, 'r')
    input1 = input1.read()
    input1 = input1.split(' ')
    return input1

class Marbles:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.number = 0
        self.counterclockwise = 0
        self.clockwise = 0

class Game:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.current_marble = 0
        self.marble_in_play = 1
        self.current_player = 0
    
    def play_routine(self):
        marbles_dict[self.marble_in_play] = Marbles()
        marbles_dict[self.marble_in_play].number = self.marble_in_play
        marbles_dict[self.marble_in_play].clockwise = marbles_dict[marbles_dict[self.current_marble].clockwise].clockwise
        marbles_dict[marbles_dict[self.marble_in_play].clockwise].counterclockwise = self.marble_in_play
        marbles_dict[self.marble_in_play].counterclockwise = marbles_dict[self.current_marble].clockwise
        marbles_dict[marbles_dict[self.current_marble].clockwise].clockwise = self.marble_in_play
        self.current_marble = self.marble_in_play
        
    def play_23(self):
        Player._registry[self.current_player].score += self.marble_in_play
        pos_to_remove = self.current_marble
        for b in range(0,7):
            pos_to_remove = marbles_dict[pos_to_remove].counterclockwise
        Player._registry[self.current_player].score += marbles_dict[pos_to_remove].number
        marbles_dict[marbles_dict[pos_to_remove].clockwise].counterclockwise = marbles_dict[pos_to_remove].counterclockwise
        marbles_dict[marbles_dict[pos_to_remove].counterclockwise].clockwise = marbles_dict[pos_to_remove].clockwise
        self.current_marble = marbles_dict[pos_to_remove].clockwise
        marbles_dict[pos_to_remove].clockwise = ''
        marbles_dict[pos_to_remove].counterclockwise = ''
 
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
total_marbles = int(parameters[6]) * 100

Game()

marbles_dict = {}

for a in range(0,player_count):
    Player()

marbles_dict[0] = Marbles()

for a in range(1,total_marbles):
    Game._registry[0].determine_play()

max_score = Player._registry[0].score

for a in range(1,player_count):
    if Player._registry[a].score > max_score:
        max_score = Player._registry[a].score

print("9b: " + str(max_score))
