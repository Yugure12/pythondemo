import turtle

def draw_fractal_triangle(t, order, size):
    if order == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        size /= 2
        draw_fractal_triangle(t, order - 1, size)
        t.forward(size)
        draw_fractal_triangle(t, order - 1, size)
        t.backward(size)
        t.left(60)
        t.forward(size)
        t.right(60)
        draw_fractal_triangle(t, order - 1, size)
        t.left(60)
        t.backward(size)
        t.right(60)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.color("blue")
    t.width(2)

    order = 4  # 分形三角形的阶数
    size = 300  # 初始三角形的大小

    t.penup()
    t.goto(-size / 2, -size / 2)
    t.pendown()

    draw_fractal_triangle(t, order, size)

    t.hideturtle()
    screen.exitonclick()

if __name__ == "__main__":
    main()
