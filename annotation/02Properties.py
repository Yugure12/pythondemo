# 方法调用转属性调用

"""
    将方法的调用方式改变成”属性调用“，即增加getter/setter方法。
"""


class Human:
    @property
    def salary(self):
        print("salary run")
        return 3000


h = Human()
# e.salary() #正常使用，调用e对象的salary()方法
print(h.salary)


"""
    这里是对象可以直接操作对象的属性。下一步，会将name、salary属性设置成私有，然后通过get、set方法来操作。
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee = Employee("name", 1000)
print(employee.salary, employee.name)
employee.salary = 2000
print(employee.salary, employee.name)

"""
    将对象属性设置为私有
"""


class Emp:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("输入错误！")


emp = Emp("haha", 100)
print(emp.get_salary())
emp.set_salary(2000)
print(emp.get_salary())


# 通过@property注解

"""
    仍然是通过【对象.属性】这种方式调用。
    但是，因为通过@property注解标明了get方法，通过@salary.setter注解注明了set方法，
    所以后面使用时，如果是赋值操作，操作的就是set方法，如果不赋值，那就是get方法。
"""

class User:

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary


    @salary.setter
    def salary(self, salary):
        if 1000 < salary < 50000:
            self.__salary = salary
        else:
            print("输入错误！")

user = User("user", 1000)
print(user.salary)
user.salary = -100
print(user.salary)