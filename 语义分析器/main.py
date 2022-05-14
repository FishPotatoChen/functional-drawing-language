# -*- coding: utf-8 -*-
"""
Created on Wed Dec 3 18:27:18 2020

@author: 陈芊宇 学号：18130500273

Copyright (c) 2020 陈芊宇 All rights reserved.
"""

import os

from myparser import Parser

if __name__ == '__main__':
    print('state_of_origin, state_of_scale, state_of_rot, state_of_for, draw')
    path = os.getcwd()
    Parser(path+r'\test.txt').analyze()
