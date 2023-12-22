# 测试参数的类型：位置参数、默认值参数、命名参数


def test01(a, b, c, d):
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


def test02(a, b, c=10, d=15):
    print("{0}-{1}-{2}-{3}".format(a, b, c, d))


test01(10, 20, 30, 40)

# 参数的位置不影响赋值逻辑
test01(d=10, c=20, b=30, a=40)

# 不传，就用默认值
test02(2, 3)
test02(2, 3, 4)

# 可变参数


# 可变参数之元组
def f1(a, b, *c):
    print(a, b, c)


f1(8, 9, 10, 11)


# 可变参数之字典
def f2(a, b, **c):
    print(a, b, c)


f2(8, 9, name="gaoqi", age=18)


# 可变参数
def f3(a, b, *c, **d):
    print(a, b, c, d)


f3(8, 9, 10, 11, 12, name="gaoqi", age=18)

# 可变参数后面的参数必须“强制命名参数”


def f4(*a, b, c):
    print(a, b, c)


f4(1, 2, b=3, c=4)
