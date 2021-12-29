#DCS Day 9

class Game:

    def __init__(self,a,b):
        self.positions = [a,b]
        self.scores = [0,0]
        self.current_dice_position = 1
        self.die_roll_count = 0

    def do_turn(self,x):
        y = (3 * self.current_dice_position) + 3
        self.positions[x - 1] = (self.positions[x - 1] + y) % 10
        if self.positions[x - 1] == 0:
            self.positions[x - 1] = 10
        self.scores[x - 1] += self.positions[x-1]
        self.current_dice_position += 3
        self.current_dice_position = self.current_dice_position % 100
        self.die_roll_count += 3
        
    def play_game_21a(self):
        game_state = 1
        while self.scores[0] < 1000 and self.scores[1] < 1000:
            if game_state > 0:
                self.do_turn(1)
            else:
                self.do_turn(2)
            game_state *= -1
        print("21A: " + str(min(self.scores) * self.die_roll_count))

my_game = Game(2,7)
my_game.play_game_21a()

