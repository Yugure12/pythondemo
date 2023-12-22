# 测试nonlocal，global关键字用法

a = 1000
def outer():
    b = 10

    def inner():
        nonlocal b # 声明外部函数的局部变量
        print("inner b：", b)
        b = 20

        global a
        a = 100

    inner()
    print("outer b：", b)

outer()
print(a)