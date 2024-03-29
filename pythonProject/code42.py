
# 元组 => 功能和列表类似

# 1.创建元组
a = ()
print(type(a))
b = tuple()
print(type(b))
print('---------------------')
# 2.创建元组的时候指定初始值
# 使用()来打印元组
a = (1, 2, 3, 4)
print(a)
print('---------------------')

# 3.元组中的元素也可以是任意类型
a = (1, 2, 'hello', True, [])
print(a)
print('---------------------')

# 4.通过下标访问元组中的元素 下标从0开始到len-1结束
a = (1, 2, 3, 4)
print(a[1])
print(a[-1])
# print(a[100])
print('---------------------')

# 5.通过切片来获取元组中的一个部分 操作和列表一样
a = (1, 2, 3, 4)
# 结果是2 3
print(a[1: 3])
print('---------------------')

# 6.使用for循环来遍历元组 下标和while一样都和列表相似
a = (1, 2, 3, 4)
for elem in a:
    print(elem)
print('---------------------')

# 7.使用in 判定元素是否存在 使用index查找元素下标
a = (1, 2, 3, 4)
print(3 in a)
print(a.index(3))
print('---------------------')

# 8.使用+来拼接两个元组
a = (1, 2, 3, 4)
b = (5, 6, 7, 8)
print(a + b)
print(b)
print('---------------------')

# 9.元组只能支持读操作 不支持修改操作
a = (1, 2, 3, 4)
# a[0] = 100
# a.append(5)
print(a)
print('---------------------')

# 10.进行多元赋值的时候 本质上是用元组的方式进行工作的
def getPoint():
    x = 10
    y = 20
    return x, y


x, y = getPoint()          # 构成一个新的元组
print(type(getPoint()))