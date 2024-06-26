# -*- coding: utf-8 -*-
"""
Created on Wed Dec 4 11:12:17 2020

@author: 陈芊宇 学号：18130500273

Copyright (c) 2020 陈芊宇 All rights reserved.
"""

# 编译器

import myparser


class Compile():
    def __init__(self, input_path, output_path):
        self.path = output_path
        self.MidCode = myparser.Parser(input_path).analyze()
        with open(self.path, 'w', encoding='utf-8') as f:
            # 增加头文件，即turtle库
            f.write(
                '''# @author: 陈芊宇 学号：18130500273
# Copyright (c) 2020 陈芊宇 All rights reserved.

import math
import turtle

import numpy as np

# 初始化画布
turtle.setup(width=1.0,height=1.0)
turtle.penup()
'''
            )

    def create(self):
        with open(self.path, 'a', encoding='utf-8') as f:
            # 操作每一次画图
            for i in self.MidCode:
                f.write(
                    '''
# 绘图
for T in np.arange('''+str(i[3][0])+''', '''+str(i[3][1])+''', '''+str(i[3][2])+'''):
    x = '''+str(i[4][0])+'''*'''+str(i[1][0])+'''
    y = '''+str(i[4][1])+'''*'''+str(i[1][1])+'''
    x_rot = x*math.cos('''+str(i[2])+''')+y*math.sin('''+str(i[2])+''')+'''+str(i[0][0])+'''
    y_rot = y*math.cos('''+str(i[2])+''')-x*math.sin('''+str(i[2])+''')+'''+str(i[0][1])+'''
    turtle.goto(x_rot,y_rot)
    turtle.dot()
'''
                )
            f.write('\nturtle.done()')
