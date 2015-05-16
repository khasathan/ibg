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
        expect = ['a', 'b', 'c']
        actual = self.solver.number_to_char_array([0, 1, 2])
        self.assertEqual(actual, expect)

    def test_string_to_char_array(self):
        expect = ['a', 'b', 'c']
        actual = self.solver.string_to_char_array('abc')
        self.assertEqual(actual, expect)

    def test_dec_to_letters(self):
        expect = 'kor'
        actual = self.solver.dec_to_letters(7141)
        self.assertEqual(actual, expect)

    def test_letters_to_dec(self):
        expect = 7141
        actual = self.solver.letters_to_dec('kor')
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()
