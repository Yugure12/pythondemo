# 嵌套函数、内部函数

def f1():
    print("f1 running")

    def f2():
        print("f2 running")

    f2()

f1()