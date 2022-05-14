# -*- coding: utf-8 -*-
"""
Created on Wed Dec 4 11:12:45 2020

@author: 陈芊宇 学号：18130500273

Copyright (c) 2020 陈芊宇 All rights reserved.
"""

import os

import mycompile

if __name__ == '__main__':
    path = os.getcwd()
    mycompile.Compile(path+r'\test.txt', path+r'\output.py').create()
