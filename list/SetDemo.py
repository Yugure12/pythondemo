# 1. 创建一个集合
my_set = {1, 2, 3}

# 2. 添加元素
my_set.add(4)

# 3. 移除元素
my_set.remove(2)  # 如果元素不存在会引发 KeyError
my_set.discard(5)  # 安全地移除元素，即使元素不存在也不会引发错误

# 4. 清空集合
my_set.clear()

# 5. 复制集合
new_set = my_set.copy()

# 6. 集合的长度
length = len(my_set)

# 7. 检查元素是否存在
if 3 in my_set:
    print("元素 3 存在于集合中")

# 8. 集合的迭代
for item in my_set:
    print(item)

# 9. 集合的并集
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # 或使用 union_set = set1.union(set2)

# 10. 集合的交集
intersection_set = set1 & set2  # 或使用 intersection_set = set1.intersection(set2)

# 11. 集合的差集
difference_set = set1 - set2  # 或使用 difference_set = set1.difference(set2)

# 12. 集合的对称差集
symmetric_difference_set = set1 ^ set2  # 或使用 symmetric_difference_set = set1.symmetric_difference(set2)

# 13. 判断子集和超集
is_subset = set1.issubset(set2)
is_superset = set1.issuperset(set2)

# 14. 删除指定元素
my_set.discard(4)

# 15. 移除并返回任意元素
popped_element = my_set.pop()

# 16. 冻结集合（只读集合，不可更改）
frozen_set = frozenset(my_set)
