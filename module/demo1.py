"""
什么是模块：
    只要是以.py为后缀的文件，都可以称为模块

模块中可以保存什么东西？
    1、变量
    2、函数
    3、面向对象（类、对象）
    4、可执行代码块

使用模块有什么好处？
    管理方便；易维护
    降低复杂度

如何使用模块：
    自定义模块
    导入模块：
        1、import 模块名1，模块2
            导入之后如何使用？
                模块名.变量
                模块名.类
                模块名.函数名(参数)

        2、导入模块中相关数据 from 模块 import 变量、函数、类
            导入之后如何使用？
                可以直接使用
"""

PI = 3.14


def get_area(r):
    """
    求圆面积的方法
    :param r: 半径
    :return: 面积
    """
    return PI * r * r


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self) :
        """
        展示学生信息
        :return:  None
        """
        print("name:%s age:%d" % (self.name, self.age))


print(PI)
print(get_area(10))
Student("a", 10).show_info()


# 1、导入模块的方式
# import random
# result = random.randint(1, 6)
# print(result)

# 2、导入模块中相关数据的方式
from random import randint

result = randint(1, 6)
print(result)