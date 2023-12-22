# 析构方法

class Person:

    def __init__(self):
        print("创建对象：{0}".format(id(self)))

    def __del__(self):
        print("销毁对象：{0}".format(id(self)))


p1 = Person()
p2 = Person()
del p2

print(p1)
print(p2)