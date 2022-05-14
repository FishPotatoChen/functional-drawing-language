# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:05:45 2020

@author: 陈芊宇 学号：18130500273

Copyright (c) 2020 陈芊宇 All rights reserved.
"""

import os

import scanner

if __name__ == "__main__":
    # print("输入\t类型\t\t\t值\t\t函数")
    path = os.getcwd()
    scan = scanner.Scanner(path+r'\test.txt')
    scan.analyze()
