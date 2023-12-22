# 静态方法

"""
    @classmethod 作用是将一个方法标记为类方法，允许在不创建对象的情况下直接调用该方法。

    像Student.add(1, 2)，则是直接使用Student类的add方法；
    像Student.sub(3, 2)，是先生成了一个Student对象，再调用该对象的sub方法。
"""


class Student:
    @classmethod
    def add(cls, a, b):  # 静态方法
        print("{0} + {1} = {2}".format(a, b, a + b))
        return a + b

    def sub(a, b):
        print("{0} - {1} = {2}".format(a, b, a - b))
        return a - b


Student.add(1, 2)
Student.sub(3, 2)