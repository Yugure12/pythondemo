"""
用turtle画一个棋盘
"""

import turtle

pen = turtle.Pen()
pen.speed(10)

width = 30
num = 18

x = [(-400, 400), (-400 + width * num, 400)]
y = [(-400, -400), (-400, 400 - width * num)]


