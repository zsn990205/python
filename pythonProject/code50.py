
f = open('E:/Python环境/test.txt', 'w')
f.write('床前明月光\n')
f.write('疑是地上霜\n')
f.write('举头望明月\n')
f.write('低头思故乡')
f.close()

# 1.使用read来读文件内容,指定读几个字符
# f = open('E:/Python环境/test.txt', 'r')
# ret = f.read(2)
# print(ret)
# f.close()

# 2.更常见的需求是按行读取
# 最简单的方法是for循环
# f = open('E:/Python环境/test.txt', 'r')
# for line in f:
#     print(f'line = {line}', end='')
# f.close()

# 3.还可以使用readlines方法直接把整个文件所有内容都读出来
# 按照行组织在一个列表中
f = open('E:/Python环境/test.txt', 'r')
lines = f.readlines()
print(lines)
f.close()