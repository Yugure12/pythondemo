# 1. 创建一个元组
my_tuple = (1, 2, 3)

# 2. 访问元组元素
first_element = my_tuple[0]
second_element = my_tuple[1]

# 3. 切片操作
subset = my_tuple[1:3]  # 获取索引 1 和 2 的元素

# 4. 元组拼接
combined_tuple = my_tuple + (4, 5, 6)

# 5. 元组重复
repeated_tuple = my_tuple * 3

# 6. 获取元组长度
length = len(my_tuple)

# 7. 检查元素是否存在
if 2 in my_tuple:
    print("元素 2 存在于元组中")

# 8. 迭代元组
for item in my_tuple:
    print(item)

# 9. 转换为列表
my_list = list(my_tuple)

# 10. 元组解包
a, b, c = my_tuple  # 将元组中的值分配给变量 a, b, c

# 11. 获取元组中某个元素的索引
index = my_tuple.index(2)  # 获取元素 2 的索引

# 12. 统计元素出现的次数
count = my_tuple.count(2)  # 统计元素 2 出现的次数

# 13. 比较元组
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
are_equal = tuple1 == tuple2  # 比较两个元组是否相等

# 14. 创建包含单个元素的元组
single_element_tuple = (42,)  # 请注意逗号的存在，用于区分元组和表达式
