# 测试多态


class Man:
    def eat(self):
        print("饿了，次饭了。")


class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")


class English(Man):
    def eat(self):
        print("英国人用叉子吃饭")


class Indian(Man):
    def eat(self):
        print("印度人用右手吃饭")


def manEat(m):
    if isinstance(m, Man):
        m.eat()
    else:
        print("不能吃饭")

manEat(Chinese())