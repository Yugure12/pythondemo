# 测试全局变量、局部变量
import time

a = 3  # 全局变量


def test01():
    b = 4  # 局部变量
    print(b * 10)

    global a  # 如果要在函数内改变全局变量的值，增加global关键字声明
    print(a)
    a = 300

    print(locals())  # 打印输出的局部变量
    print(globals())  # 打印输出的全局变量


test01()
print(a)


# 测试全局变量、局部变量的效率

import math


def test001():
    start = time.time()
    for i in range(10000000):
        math.sqrt(30)
    end = time.time()
    print("耗时 {0} ms".format(end - start))


def test002():
    b = math.sqrt
    start = time.time()
    for i in range(10000000):
        b(30)
    end = time.time()
    print("耗时 {0} ms".format(end - start))

test001()
test002()