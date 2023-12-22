# 测试函数的定义和调用
def test01():
    print("*" * 10)
    print("@" * 10)


test01()


# 返回较大的值
def getMax(a, b):
    # 比较大小
    if a > b:
        print(a, "较大值")
    else:
        print(b, "较大值")


getMax(30, 20)


# 测试函数 也是对象
def test01():
    print("hhhh")

c = test01()

test01()
c()
