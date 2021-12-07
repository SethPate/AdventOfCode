#DCS Day 4

def fileimport(input_file1):
    input1 = open(input_file1, 'r')
    input1 = input1.read()
    return input1

def listmaker(a):
    b = a.split("\n")
    return b

class Board:
    def __init__(self, row_1, row_2, row_3, row_4, row_5):
        self.position_list = []
        self.bingo_board_lol = [row_1,row_2,row_3,row_4,row_5]
        self.bingo_board_list = []
        self.playlist = []
        self.winner_condition_list = [0,0,0,0,0,0,0,0,0,0]
        self.winner_status = 'no'

    def bingo_play(self,input_value):
        current_row = -1
        current_column = -1
        if input_value in self.bingo_board_lol[0]:
            current_row = 0
            current_column = self.bingo_board_lol[0].index(input_value)
        elif input_value in self.bingo_board_lol[1]:
            current_row = 1
            current_column = self.bingo_board_lol[1].index(input_value)
        elif input_value in self.bingo_board_lol[2]:
            current_row = 2
            current_column = self.bingo_board_lol[2].index(input_value)
        elif input_value in self.bingo_board_lol[3]:
            current_row = 3
            current_column = self.bingo_board_lol[3].index(input_value)
        elif input_value in self.bingo_board_lol[4]:
            current_row = 4
            current_column = self.bingo_board_lol[4].index(input_value)
        if current_row > -1 and current_column > -1:
            new_play = current_row * 5 + current_column
            self.winner_condition_list[current_row] += 1
            self.winner_condition_list[current_column + 5] += 1
            self.playlist.append(input_value)

    def did_i_win(self):
        if 5 in self.winner_condition_list and self.winner_status == 'no':
            self.winner_status = 'yes'

    def score_board(self):
        board_score = 0

        for k in range(0,5):
            for j in range(0,5):
                self.bingo_board_list.append(self.bingo_board_lol[k][j])
        for k in range(0,len(self.bingo_board_list)):
            if self.bingo_board_list[k] not in self.playlist:
                board_score += int(self.bingo_board_list[k])
        return board_score

data_input = fileimport('day4_input.txt')
input_list = listmaker(data_input)

gameplay_sequence = input_list[0].split(",")
input_list.pop(0)

#4A

board_list = []
board_counter = 0

for i in range(0,len(input_list)):
    if input_list[i] != '' and (i + 5) % 6 == 0:
        board_list.append(Board(input_list[i].split(),input_list[i+1].split(),input_list[i+2].split(),input_list[i+3].split(),input_list[i+4].split()))
        board_counter += 1

game_status = 1

#print(len(board_list))
#print(gameplay_sequence)

last_call = -1
winner_number = -1

for item in gameplay_sequence:
    if game_status == 0:
        break
    for i in range(0,len(board_list)):
        board_list[i].bingo_play(str(item))
        last_call = int(item)
    for i in range(0,len(board_list)):
        board_list[i].did_i_win()
        if board_list[i].winner_status == 'yes':
            game_status = 0
            winner_number = i
            
winning_board_score = int(board_list[winner_number].score_board())

print("4A: " + str(winning_board_score * last_call))

#4B

board_list_4b = []
board_counter = 0

for i in range(0,len(input_list)):
    if input_list[i] != '' and (i + 5) % 6 == 0:
        board_list_4b.append(Board(input_list[i].split(),input_list[i+1].split(),input_list[i+2].split(),input_list[i+3].split(),input_list[i+4].split()))
        board_counter += 1

last_call = -1
win_sequence_list = []

for item in gameplay_sequence:
    if len(win_sequence_list) == len(board_list_4b):
        break
    for i in range(0,len(board_list_4b)):
        board_list_4b[i].bingo_play(str(item))
        last_call = int(item)
    for i in range(0,len(board_list_4b)):
        board_list_4b[i].did_i_win()
        if board_list_4b[i].winner_status == 'yes' and i not in win_sequence_list:
            win_sequence_list.append(i)
            
winning_board_score_4b = int(board_list_4b[win_sequence_list[-1]].score_board())

print("4B: " + str(winning_board_score_4b * last_call))

