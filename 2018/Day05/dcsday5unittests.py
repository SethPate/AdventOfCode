from dcsday5 import char_comp, remake_string, polymerize, get_unit_type_list
import unittest

class MyTest(unittest.TestCase):    
    def test_char_comp(self):
        input_text_a = 'a'
        input_text_b = 'a'
        expected_result = 2
        self.assertEqual(char_comp(input_text_a,input_text_b),expected_result)
    
    def test_polymerize(self):
        input_text = ['d', 'a', 'b', 'A', 'c', 'C', 'a', 'C', 'B', 'A', 'c', 'C', 'c', 'a', 'D', 'A']
        expected_result = ['d', 'a', 'b', 'C', 'B', 'A', 'c', 'a', 'D', 'A']
        self.assertEqual(polymerize(input_text),expected_result)
    
    def test_remake_string(self):
        input_list = ['a','b','c']
        expected_result = 'abc'
        self.assertEqual(remake_string(input_list),expected_result)
    
    def test_get_unit_type_list(self):
        input_text = ['d', 'a', 'b', 'A', 'c', 'C', 'a', 'C', 'B', 'A', 'c', 'C', 'c', 'a', 'D', 'A']
        expected_result = ['D','A','B','C']
        self.assertEqual(get_unit_type_list(input_text),expected_result)
    
if __name__ == '__main__':
    unittest.main()

