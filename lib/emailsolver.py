#-*- coding: utf-8 -*-

'''
@author: khasathan[AT]gmail[DOT]com
'''

import math

class EmailSolver():
    def __init__(self):
        self.CHAR_MAP = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
            'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
            'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
            'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
            'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
            'z': 25
        }

        '''Swap keys and values in CHAR_MAP
        ex. { 0: 'a', 1: 'b', 2: 'c' ... }
        '''
        self.NUM_MAP = dict(zip(self.CHAR_MAP.values(), self.CHAR_MAP.keys()))
        
        self.LETTERS_BASE = 26

    def number_to_char_array(self, num_array):
        result = []
        for num in num_array:
            result.append(self.NUM_MAP[num])
        return result

    def string_to_char_array(self, string):
        return [char for char in string]

    def dec_to_letters(self, decimal):
        result = []
        if decimal == 0:
            return 0
        while decimal != 0:
            reminder = (decimal % self.LETTERS_BASE)
            decimal = int(math.floor(decimal / self.LETTERS_BASE))
            result = [reminder] + result
        return ''.join(self.number_to_char_array(result))

    def letters_to_dec(self, letters):
        result = 0
        char_array = self.string_to_char_array(letters)
        factor = len(char_array) - 1
        for char in char_array:
            result += self.CHAR_MAP[char] * (self.LETTERS_BASE ** factor)
            factor -= 1
        return result
