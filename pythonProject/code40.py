
# 1.使用pop删除列表中最末尾的元素
a = [1, 2, 3, 4]
a.pop()
print(a)
print('---------------------')

# 2.使用pop删除任意位置的元素 pop的参数可以传一个下标过去
a = [1, 2, 3, 4]
# 删除下标为1的元素->2
a.pop(1)
print(a)
print('---------------------')

# 3.使用remove方法,可以按照值来进行删除
a = ['aa', 'bb', 'cc', 'dd']
# 删除字符串cc
a.remove('cc')
print(a)