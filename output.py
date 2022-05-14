# @author: 陈芊宇 学号：18130500273
# Copyright (c) 2020 陈芊宇 All rights reserved.

import math
import turtle

import numpy as np

# 初始化画布
turtle.setup(width=1.0,height=1.0)
turtle.penup()

# 绘图
for T in np.arange(0, 6.283185307179586, 0.06283185307179587):
    x = math.cos(T)*100
    y = math.sin(T)*100
    x_rot = x*math.cos(0)+y*math.sin(0)+0
    y_rot = y*math.cos(0)-x*math.sin(0)+0
    turtle.goto(x_rot,y_rot)
    turtle.dot()

# 绘图
for T in np.arange(0, 6.283185307179586, 0.06283185307179587):
    x = math.cos(T)*50.0
    y = math.sin(T)*100
    x_rot = x*math.cos(1.5707963267948966)+y*math.sin(1.5707963267948966)+100
    y_rot = y*math.cos(1.5707963267948966)-x*math.sin(1.5707963267948966)+0
    turtle.goto(x_rot,y_rot)
    turtle.dot()

turtle.done()