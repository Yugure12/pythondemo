# 深拷贝、浅拷贝

import copy

a = [10, 20, [5, 6]]
b = copy.copy(a)  # 浅拷贝

print("a：", a)
print("b：", b)

b.append(30)
b[2].append(7)

print("a：", a)
print("b：", b)

c = copy.deepcopy(a)
c.append(40)
c[2].append(10)

print("a：", a)
print("c：", c)
