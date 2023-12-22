# 测试递归函数的基本原理


def test01():
    print("test01")


def test02():
    print("test02")


test01()

# 5 的递归处理

total = 1


def recursive(a):
    if a == 1:
        return 1
    return a * recursive(a - 1)


print(recursive(5))
