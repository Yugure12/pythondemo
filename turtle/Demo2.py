"""
用turtle画一个正方形并计算面积。
"""

import math

import turtle

# 定义多个点
x1,y1 = 100, 100
x2,y2 = 100,-100
x3,y3 = -100,-100
x4,y4 = -100,100

# 绘制折线
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

# 根号 长的2次方 * 款的2次方
distance = math.sqrt((x1-x4)**2 + (y1 - y4)**2)
turtle.write(distance)

turtle.done()