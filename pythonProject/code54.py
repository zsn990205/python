
# 5.实现一个文件查找工具
# 输入要查找的路径,输入要查找的文件名(一部分)
# 自动的在指定的路径中进行查找

import os
inputPath = input('请输入您要搜索的路径: ')
pattern = input('请输入您要查找的关键词: ')

for dirpath, dirnames, filenames in os.walk(inputPath):
    for f in filenames:
        if pattern in f:
            print(f'{dirpath}/{f}')
