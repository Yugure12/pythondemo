"""
导入自定义模块：
    1、import模块：
        问题：在导入模块的时候，模块中的代码会被执行一遍；
        解决：在自定义模块中，新增控制代码：
            if __name__ = "__main__"
                测试代码执行
    2、from 模块 import 函数
        问题：如果使用这种方法导入模块中的功能，一个个填写会比较麻烦。
        解决：可以使用*，导入模块中的所有功能。
        * 默认导入所有功能，如果在自定义模块中，使用__all__ = ["add", "sub"]，则只导入add和sub两个功能。（python3环境下，不提倡使用）
"""

# import Math
# print("和：%s" % Math.add(1, 2))

# from Math import add,sub,mul,div
# print("和：%s" % add(1,3))

from Math import *
print("和：%s" % add(1,3))
print("差：%s" % sub(1,3))