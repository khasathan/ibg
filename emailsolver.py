#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
@author: khasathan[AT]gmail[DOT]com
'''

import unittest
from lib import emailsolver

def main():
    solver = emailsolver.EmailSolver()

    dota_ = solver.letters_to_dec('dota')
    is_ = solver.letters_to_dec('is')
    ijlegcod_ = solver.letters_to_dec('ijlegcod')
    a_ = solver.letters_to_dec('a')
    #game_ = solver.letters_to_dec('game')
    #of_ = solver.letters_to_dec('of')
    #love_ = solver.letters_to_dec('love')
    b_ = solver.letters_to_dec('b')
    zanroo_ = solver.letters_to_dec('zanroo')
    tmfafj_ = solver.letters_to_dec('tmfafj')

    '''
     Expression:
     [([dota + is + ijlegcod] / [a * (game ^ of ^ love) + b]) * zanroo] + tmfafj
     We can ignore [a * (game ^ of ^ love) + b]. We know that a=0, b=1.
     So, we get this [0 * (game ^ of ^ love) / 1] = 1
    '''
    answer_dec = ((dota_ + is_ + ijlegcod_) * zanroo_) + tmfafj_
    answer_letters = solver.dec_to_letters(answer_dec)

    print('Answer: ', end='')
    print('{email_name}@xxxcompany.com'.format(email_name=answer_letters))

if __name__ == '__main__':
    main()
