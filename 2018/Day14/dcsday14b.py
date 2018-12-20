#dan day 14

import sys

input_14a = 380621

def make_new_recipes(a):
    recipe_sum = recipe_set[a[0].recipe_set_key].number + recipe_set[a[1].recipe_set_key].number
    recipe_list = list(str(recipe_sum))
    return recipe_list

def convert_list_to_string(a,d):
    for c in range(0,len(a)):
        d = str(d) + str(a[c])
    return d
        
class Board:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.length = 2
        self.input_text = str(input_14a)
        self.input_length = len(self.input_text)

    def expand_recipes(self):
        for c in range(0,len(new_recipe_list)):
            recipe_set[self.length] = Recipe()
            recipe_set[self.length].set_key = self.length
            recipe_set[self.length].number = int(new_recipe_list[c])
            recipe_set[self.length - 1].right_set_key = recipe_set[self.length].set_key
            if self.check_equals() == self.input_length:
                print "IT'S OVER"
                print "14b: " + str(self.length + 1 - self.input_length)
                sys.exit()
            self.length += 1
            
    def check_equals(self):
        if self.length > self.input_length:
            match_score = 0
            for k in range(0,self.input_length):
                if str(recipe_set[self.length - k].number) <> str(self.input_text[self.input_length - k - 1:self.input_length - k]):
                    return match_score
                    break
                else:
                    match_score += 1
            return match_score
        
class Elf:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.name = ''
        self.recipe_set_key = 0
    
    def move_it(self):
        move_count = recipe_set[self.recipe_set_key].number + 1
        for a in range(0,move_count):
            self.recipe_set_key = recipe_set[self.recipe_set_key].right_set_key
        recipe_set[self.recipe_set_key].elf = self.name

class Recipe:
    
    def __init__(self):
        self.set_key = 0
        self.number = 0
        self.right_set_key = 0
        self.elf = 'none'
    
    def print_details(self):
        print("this is number " + str(self.number))
        print("this is set key " + str(self.set_key))
        print("to the right is set key " + str(self.right_set_key))


#initialize everything
Board()

Elf()
Elf()


Elf._registry[0].name = 0
Elf._registry[0].recipe_set_key = 0
Elf._registry[1].name = 1
Elf._registry[1].recipe_set_key = 1

recipe_set = {}

recipe_set[0] = Recipe()
recipe_set[0].number = 3
recipe_set[0].elf = 0
recipe_set[0].set_key = 0

recipe_set[1] = Recipe()
recipe_set[1].number = 7
recipe_set[1].elf = 1
recipe_set[1].set_key = 1

recipe_set[0].right_set_key = recipe_set[1].set_key

recipe_set[1].right_set_key = recipe_set[0].set_key

string_14a = '37'

recipe_counter = 2

while True:
    new_recipe_list = make_new_recipes(Elf._registry)
    Board._registry[0].expand_recipes()
    if Board._registry[0].length % 1000000 == 0:
        print Board._registry[0].length
    for item in Elf._registry:
        item.move_it()
        
