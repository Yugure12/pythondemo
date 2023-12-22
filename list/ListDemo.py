# 1. 创建一个空列表
my_list = []

# 2. 添加元素到列表末尾
my_list.append(1)
my_list.append(2)

# 3. 插入元素到指定位置
my_list.insert(1, 3)

# 4. 获取列表元素
element = my_list[0]

# 5. 修改列表元素
my_list[0] = 10

# 6. 删除指定元素
my_list.remove(2)

# 7. 删除指定位置的元素
removed_element = my_list.pop(1)

# 8. 获取列表长度
length = len(my_list)

# 9. 检查元素是否存在
if 3 in my_list:
    print("3 存在于列表中")

# 10. 查找元素的索引
index = my_list.index(10)

# 11. 统计元素出现的次数
count = my_list.count(10)

# 12. 切片操作
subset = my_list[1:3]

# 13. 迭代列表
for item in my_list:
    print(item)

# 14. 列表的排序
my_list.sort()  # 升序排序
my_list.sort(reverse=True)  # 降序排序

# 15. 反转列表
my_list.reverse()

# 16. 清空列表
my_list.clear()

# 17. 复制列表
new_list = my_list.copy()

# 18. 连接两个列表
combined_list = my_list + new_list

# 19. 列表推导
squared_list = [x**2 for x in my_list]

# 20. 使用 `enumerate` 迭代同时获取索引和值
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
