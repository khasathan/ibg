#-*- coding: utf-8 -*-

'''
@author: khasathan[AT]gmail[DOT]com
'''

import unittest
from lib import emailsolver

class EmailSolverTest(unittest.TestCase):
    def setUp(self):
        self.solver = emailsolver.EmailSolver()

    def test_number_to_char_array(self):
        expect = [
            self.solver.NUM_MAP[0],
            self.solver.NUM_MAP[1],
            self.solver.NUM_MAP[2]
        ]
        actual = self.solver.number_to_char_array([0, 1, 2])
        self.assertEqual(actual, expect)

    def test_string_to_char_array(self):
        expect = ['a', 'b', 'c']
        actual = self.solver.string_to_char_array('abc')
        self.assertEqual(actual, expect)

    def test_dec_to_letters(self):
        self.assertEqual(self.solver.dec_to_letters(1208), 'bum')

    def test_letters_to_dec(self):
        self.assertEqual(self.solver.letters_to_dec('bum'), 1208)

if __name__ == '__main__':
    unittest.main()
