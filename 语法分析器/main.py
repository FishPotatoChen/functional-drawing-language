# -*- coding: utf-8 -*-
"""
Created on Wed Dec 3 18:27:18 2020

@author: 陈芊宇 学号：18130500273

Copyright (c) 2020 陈芊宇 All rights reserved.
"""

import os

from myparser import Parser

if __name__ == '__main__':
    path = os.getcwd()
    Parser(path+r'\test.txt').analyze()
