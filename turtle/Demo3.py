"""
用turtle画一个同心圆
"""

import turtle

t = turtle.Pen()

my_colors = ["red", "green", "yellow", "black"]

t.width(3)
t.speed(10)

for x in range(10):
    t.penup()
    t.goto(0, -x*10)
    t.pendown()
    t.color(my_colors[x%len(my_colors)])
    t.circle(15 + x*10)


turtle.done()