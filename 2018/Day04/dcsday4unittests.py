from dcsday4 import newlinefile, harmonize_delimiters, timestamp_math,
import unittest

class MyTest(unittest.TestCase):    
    def test_harmonize_delimiters(self):
        input_text = '[1518-11-03 00:05] Guard #10 begins shift'
        expected_result = ['1518','11','03','00','05','Guard','10','begins','shift']
        self.assertEqual(harmonize_delimiters(input_text),expected_result)
    
    def test_polymerize(self):
        input_text = ['d', 'a', 'b', 'A', 'c', 'C', 'a', 'C', 'B', 'A', 'c', 'C', 'c', 'a', 'D', 'A']
        expected_result = 'dabCBAcaDA'
        self.assertEqual(polymerize
    
    def test_timestamp_math(self):
        input_text = ['1518','11','03','00','05','Guard','10','begins','shift']
        expected_result = 303.0055
        self.assertEqual(round(timestamp_math(input_text),4),round(expected_result,4))
    
if __name__ == '__main__':
    unittest.main()

