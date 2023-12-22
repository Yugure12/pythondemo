# 测试私有属性/方法


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.__age = age # 私有属性

    def __work(self): # 私有方法
        print("好好工作，好好赚钱")

e = Employee("abc", 123)
print(e.name)
# print(e.age)
print(e._Employee__age)
print(dir(e)) # 存的就是_Employee__age

e._Employee__work()
