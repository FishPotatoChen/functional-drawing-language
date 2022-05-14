# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:05:45 2020

@author: 陈芊宇 学号：18130500273

Copyright (c) 2020 陈芊宇 All rights reserved.
"""

TOKEN = {
    # 常量
    'PI': {'TYPE': 'CONST_ID', 'VALUE': 'math.pi', 'FUNCTION': None},
    'E': {'TYPE': 'CONST_ID', 'VALUE': 'math.e', 'FUNCTION': None},
    # 变量
    'T': {'TYPE': 'SYMBOL', 'VALUE': None, 'FUNCTION': None},
    # 函数
    'SIN': {'TYPE': 'FUNC', 'VALUE': None, 'FUNCTION': 'math.sin'},
    'COS': {'TYPE': 'FUNC', 'VALUE': None, 'FUNCTION': 'math.cos'},
    'TAN': {'TYPE': 'FUNC', 'VALUE': None, 'FUNCTION': 'math.tan'},
    'LN': {'TYPE': 'FUNC', 'VALUE': None, 'FUNCTION': 'math.log'},
    'EXP': {'TYPE': 'FUNC', 'VALUE': None, 'FUNCTION': 'math.exp'},
    'SQRT': {'TYPE': 'FUNC', 'VALUE': None, 'FUNCTION': 'math.sqrt'},
    # 保留字
    'ORIGIN': {'TYPE': 'KEYWORD', 'VALUE': None, 'FUNCTION': None},
    'SCALE': {'TYPE': 'KEYWORD', 'VALUE': None, 'FUNCTION': None},
    'ROT': {'TYPE': 'KEYWORD', 'VALUE': None, 'FUNCTION': None},
    'IS': {'TYPE': 'KEYWORD', 'VALUE': None, 'FUNCTION': None},
    'FOR': {'TYPE': 'KEYWORD', 'VALUE': None, 'FUNCTION': None},
    'FROM': {'TYPE': 'KEYWORD', 'VALUE': None, 'FUNCTION': None},
    'TO': {'TYPE': 'KEYWORD', 'VALUE': None, 'FUNCTION': None},
    'STEP': {'TYPE': 'KEYWORD', 'VALUE': None, 'FUNCTION': None},
    'DRAW': {'TYPE': 'KEYWORD', 'VALUE': None, 'FUNCTION': None},
    # 运算符
    '+': {'TYPE': 'OP', 'VALUE': None, 'FUNCTION': None},
    '-': {'TYPE': 'OP', 'VALUE': None, 'FUNCTION': None},
    '*': {'TYPE': 'OP', 'VALUE': None, 'FUNCTION': None},
    '/': {'TYPE': 'OP', 'VALUE': None, 'FUNCTION': None},
    '**': {'TYPE': 'OP', 'VALUE': None, 'FUNCTION': None},
    # 记号
    '(': {'TYPE': 'MARK', 'VALUE': None, 'FUNCTION': None},
    ')': {'TYPE': 'MARK', 'VALUE': None, 'FUNCTION': None},
    ',': {'TYPE': 'MARK', 'VALUE': None, 'FUNCTION': None},
    # 结束符
    ';': {'TYPE': 'END', 'VALUE': None, 'FUNCTION': None},
}
