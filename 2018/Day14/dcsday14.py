#dan day 14

input_14a = 380621

def make_new_recipes(a):
    #print "making new recipes"
    recipe_sum = recipe_set[a[0].recipe_set_key].number + recipe_set[a[1].recipe_set_key].number
    recipe_list = list(str(recipe_sum))
    #print recipe_list
    return recipe_list

def expand_recipes(a,b):
    start_length = len(a)
    for c in range(0,len(b)):
        a[start_length + c] = Recipe()
        a[start_length + c].set_key = start_length + c
        a[start_length + c].number = int(b[c])
        a[start_length + c].left_set_key = a[start_length + c - 1].set_key
        a[start_length + c - 1].right_set_key = a[start_length + c].set_key
    return a

def convert_list_to_string(a,d):
    for c in range(0,len(a)):
        d = str(d) + str(a[c])
    return d

class Elf:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.name = ''
        self.recipe_set_key = 0
    
    def move_it(self):
        move_count = recipe_set[self.recipe_set_key].number + 1
        #print "move_count: " + str(move_count)
        for a in range(0,move_count):
            self.recipe_set_key = recipe_set[self.recipe_set_key].right_set_key
            #print self.recipe_set_key
        recipe_set[self.recipe_set_key].elf = self.name
        
        
class Recipe:
    _registry = []
    
    def __init__(self):
        self._registry.append(self)
        self.set_key = 0
        self.number = 0
        self.right_set_key = 0
        self.left_set_key = 0
        self.elf = 'none'
    
    def print_details(self):
        print("this is number " + str(self.number))
        print("this is set key " + str(self.set_key))
        print("to the right is set key " + str(self.right_set_key))
        print("to the left is set key " + str(self.left_set_key))


#initialize everything
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
recipe_set[0].left_set_key = recipe_set[1].set_key

recipe_set[1].right_set_key = recipe_set[0].set_key
recipe_set[1].left_set_key = recipe_set[0].set_key

string_14a = ''

max_length_nrl = 0

#initial set expansion
while len(recipe_set) < input_14a + 10:
    new_recipe_list = make_new_recipes(Elf._registry)
    if max_length_nrl < len(new_recipe_list):
        max_length_nrl = len(new_recipe_list)
    string_14a = convert_list_to_string(new_recipe_list,string_14a)
    if len(string_14a) > 10:
        string_14a = string_14a[-10:]
    recipe_set = expand_recipes(recipe_set,new_recipe_list)

    for item in Elf._registry:
        item.move_it()
        
print string_14a
print max_length_nrl
