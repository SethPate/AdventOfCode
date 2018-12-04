import unittest
from dcsday3 import create_list_of_lists, Instruction

class MyTest(unittest.TestCase):    
    def test_create_list_of_lists(self):
        expected_solution = [[['.'], ['.']], [['.'], ['.']], [['.'], ['.']], [['.'], ['.']], [['.'], ['.']]]
        self.assertEqual(create_list_of_lists(2,5),expected_solution)
            
    def test_instruction_parse_1(self):
        test_instruction = Instruction()
        sample_instruction = '#3 @ 4,5: 6x7'
        test_instruction.instruction_parse(sample_instruction)
        self.assertEqual(test_instruction.fill_number,3)
        self.assertEqual(test_instruction.h_pos,4)
        self.assertEqual(test_instruction.v_pos,5)
        self.assertEqual(test_instruction.h_distance,6)
        self.assertEqual(test_instruction.v_distance,7)
    

if __name__ == '__main__':
    unittest.main()
