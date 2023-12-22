# 测试继承的基本使用


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_age(self):
        print("i dont know")


class Student(Person):
    def __init__(self, name, age, score):
        Person.__init__(self, name, age)  # 必须显式调用初始化父类的方法，不然计时器不会去调用
        self.score = score


# Student -> Person -> Object类
print(Student.mro())

s = Student("student", 11, 100)

s.say_age()


"""
    将Person类的age方法私有后，age变成了_Person__age。
    Student继承了Person后，同时继承了_Person__age属性。
"""
print(s._Person__age, dir(s))
 