import unittest
from dcsday2 import string_to_list, list_to_freq_table, dict_count
from dcsday2 import lev_distance, find_common_characters, checksum_calc, string_match_comp

class MyTest(unittest.TestCase):
    def test_string_to_list(self):
        example_chars = 'abcde'
        expected_outcome = ['a','b','c','d','e']
        self.assertEqual(string_to_list(example_chars), expected_outcome)
    
    def test_list_to_freq_table(self):
        sample_letters = ['a','b','c','d','d','e','e','e','e','f','f','f']
        expected_freq_table = {'a': 1, 'c': 1, 'b': 1, 'e': 4, 'd': 2, 'f': 3}
        self.assertEqual(list_to_freq_table(sample_letters),expected_freq_table)
    
    def test_dict_count(self):
        sample_letters = ['a','b','c','d','d','e','e','e','e','f','f','f']
        self.assertEqual(dict_count(list_to_freq_table(sample_letters),2),1)
    
    def test_lev_distance(self):
        self.assertEqual(lev_distance('abcdef','acddef'),2)
        
    def test_find_common_characters(self):
        self.assertEqual(find_common_characters('vwxyz','twxyh'),'wxy')
    
    def test_checksum_calc(self):
        sample_ids = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']
        self.assertEqual(checksum_calc(sample_ids,2,3),12)
    
    def test_string_match_comp(self):
        strings_to_check = ['abcde','bdget','klmno','pqrst','fguij','klmnp','wvxyz']
        self.assertEqual(string_match_comp(strings_to_check),'klmn')

if __name__ == '__main__':
    unittest.main()
    
#https://docs.python.org/3/library/unittest.html
