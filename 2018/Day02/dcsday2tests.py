#dan day2 tests

from dcsday2 import string_to_list, list_to_freq_table, dict_count
from dcsday2 import lev_distance, find_common_characters, checksum_calc, string_match_comp

#test string_to_list
string_test = 'abcde'
expected_outcome = ['a','b','c','d','e']

if string_to_list(string_test) == expected_outcome:
    print("string_to_list passes")
else:
    print("string_to_list fails")
    print(string_to_list(string_test))

#test list_to_freq_table
list_test = ['a','b','c','d','d','e','e','e','e','f','f','f']

dict_test = list_to_freq_table(list_test)

if dict_test['e'] == 4 and dict_test['b'] == 1:
    print("list_to_freq_table passes")
else:
    print("list_to_freq_table fails")

#test_dict_count

if dict_count(dict_test,2) == 1 and dict_count(dict_test,6) == 0:
    print("dict_count test passes")
else:
    print("dict_count test fails")

#test lev_distance
test_item_1 = 'abcdefg'
test_item_2 = 'bacdefh'

if lev_distance(test_item_1,test_item_2) == 3:
    print("lev_distance test passes")
else:
    print("lev_distance test fails")

#test find_common_characters

if find_common_characters('abcde','abfgh') == 'ab':
    print("find_common_characters test passes")
else:
    print("find_common_characters test fails")

#test checksum_calc

checksum_test_input = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']

if checksum_calc(checksum_test_input,2,3) == 12:
    print("checksum_calc test passes")
else:
    print("checksum_calc test fails")
    
#test string_match_comp

string_match_list = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

if string_match_comp(string_match_list) == 'fgij':
    print("string_match_comp test passes")
else:
    print(string_match_comp(string_match_list))
    print("string_match_comp test fails")
