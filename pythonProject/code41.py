
# 1.列表的拼接 使用+进行拼接
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a + b
print(c)
print('-----------------------')
c = b + a
print(c)
print(a)
print(b)
print('-----------------------')

# 2.使用extend来进行拼接的过程的时候
# 是把后一个列表的内容拼接到前一个列表里头
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = a.extend(b)
print(a)
print(b)
print(c)
print('-----------------------')

# 3.使用+=来进行拼接
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
a += b
print(a)
print(b)