import copy
class Mobile:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

class CPU:

    def calculate(self):
        print("cpu对象：", self)

class Screen:
    def show(self):
        print("screen对象：", self)

m1 = Mobile(CPU(), Screen())
m2 = m1
print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)

m2 = copy.copy(m1)
print(m2, m2.cpu, m2.screen)

m2 = copy.deepcopy(m1)
print(m2, m2.cpu, m2.screen)
