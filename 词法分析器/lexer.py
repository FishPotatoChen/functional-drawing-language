# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:05:45 2020

@author: 陈芊宇 学号：18130500273

Copyright (c) 2020 陈芊宇 All rights reserved.
"""

# 词法分析器

import re
import createtable


class Lexer:
    def __init__(self):
        # 从文件中读取记号表
        self.TOKEN = createtable.TOKEN
        self.output_list = []

    def getToken(self, sentence):
        if sentence:
            tokens = sentence.split()
            for token in tokens:
                try:
                    # No.0
                    # 首先识别直接可以识别的记号
                    # 正规式为ORIGIN|SCALE|ROT|IS|FOR|FROM|TO|STEP|DRAW|ε
                    self.output_token(token)
                    # No.0  识别结束
                except:
                    # 找不到就进入更高级的DFA中识别
                    self.argument_lexer(token)
            self.output_token(';')

    # 构造更为复杂、高级的、多种类的识别表达式
    def argument_lexer(self, argument):
        # 扫描位置
        i = 0
        # 字符串长度
        length = len(argument)
        while(i < length):
            # 临时字符串,即缓冲区
            temp = ''
            if argument[i] in ['P', 'S', 'C', 'L', 'E', 'T', '*']:
                # No.1
                # 识别"*"还是"**"的过程是一个上下文有关文法
                if argument[i] == '*':
                    i += 1
                    if i >= length:
                        self.output_token(argument[i])
                        break
                    elif argument[i] == '*':
                        self.output_token('**')
                    else:
                        i -= 1
                        self.output_token(argument[i])
                # No.1  识别结束
                else:
                    # No.2
                    # DFA判断全为字母的字符串
                    # 正规式为PI|E|T|SIN|COS|TAN|LN|EXP|SQRT
                    temp = re.findall(r"[A-Z]+", argument[i:])[0]
                    # 看该串是否接受
                    self.output_token(temp)
                    i += len(temp)-1
                    if i >= length:
                        break
                    # No.2  识别结束
            elif argument[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
                # No.3
                # 识别数字
                if argument[i] == '.':
                    # 识别开头为"."的数字
                    # 正规式为.[0-9]+
                    # 如:.52=>0.52
                    i += 1
                    temp = re.findall(r"\d+", argument[i:])[0]
                    i += len(temp)-1
                    temp = '0.' + temp
                    self.output_token(temp, False)
                else:
                    # 识别一般数字
                    # 正规式为[0-9]+.?[0-9]*
                    # 如:5.52=>5.52;12=>12
                    temp = re.findall(r"\d+\.?\d*", argument[i:])[0]
                    i += len(temp)-1
                    self.output_token(temp, False)
                if i >= length:
                    break
                # No.3   识别结束
            else:
                # No.4
                # 识别其他字符
                # 正规式为+|-|/|(|)|,|ε
                self.output_token(argument[i])
            i += 1

    # 输出函数
    # 因为解释器可以不用输出至屏幕,但是题目要求输出至屏幕
    # 所以特别写了一个函数用于输出,便于接下来的语法分析器调用文法分析器
    # 当输出不为屏幕时，将输出嵌入代码会变得不好更改
    # 如果写成独立函数，直接更改输出函数即可
    def output_token(self, token, NotNumber=True):
        if NotNumber:
            print(token, self.TOKEN[token])
        else:
            tempdic = {token: {'TYPE': 'NUMBER', 'VALUE': float(token), 'FUNCTION': None}}
            print(token, tempdic[token])
