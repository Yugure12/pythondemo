# 列表推导式
x = [x for x in range(1, 5)]
print(x)

x = [x * 2 for x in range(1, 5)]
print(x)

x = [x * 2 for x in range(1, 20) if x % 5 == 0]
print(x)
print(type(x))

x = [x for x in "abcdefg"]
print(x)

x = [(x, y) for x in range(1, 5) for y in range(10, 15)]
print(x)
print(type(x))

# 字典推导式
my_text = "i love you , i love abc, i love efg"
x = {x: my_text.count(x) for x in my_text}
print(x)

# 集合推导式
x = {x for x in range(1, 100) if x % 9 == 0}
y = [y for y in range(1, 100) if y % 9 == 0]
print(x, y)
print(type(x), type(y))

# 元组推导式 - 遍历一次后数据为空。
x = (x for x in range(10))
print(tuple(x))
print(tuple(x))
