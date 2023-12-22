# 1. 创建一个空字典
my_dict = {}

# 2. 添加键-值对
my_dict['name'] = 'Alice'
my_dict['age'] = 30

# 3. 获取值
name = my_dict['name']
age = my_dict['age']

# 4. 检查键是否存在
if 'name' in my_dict:
    print('键 "name" 存在')

# 5. 删除键-值对
del my_dict['age']

# 6. 获取所有键
keys = my_dict.keys()

# 7. 获取所有值
values = my_dict.values()

# 8. 获取所有键-值对
items = my_dict.items()

# 9. 迭代字典
for key, value in my_dict.items():
    print(f'键: {key}, 值: {value}')

# 10. 清空字典
my_dict.clear()

# 11. 复制字典
new_dict = my_dict.copy()

# 12. 获取默认值
age = my_dict.get('age', 25)

# 13. 更新字典
my_dict.update({'country': 'USA', 'city': 'New York'})