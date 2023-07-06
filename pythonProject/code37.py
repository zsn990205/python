
# 1.使用for循环进行遍历
a = [1, 2, 3, 4, 5]
for elem in a:
    print(elem)
print('-----------------------')

# 2.使用for循环,运用下标的形式
a = [1, 2, 3, 4, 5]
# len表示的是列表的长度,但是range是前闭后开的区间,所以直接写len即可
for i in range(0, len(a)):
    a[i] = a[i]+ 10
    # print(a[i])
print(a)
print('-----------------------')

# 3.使用while循环来通过下标遍历
a = [1, 2, 3, 4, 5]
i = 0
while i < len(a):
    print(a[i])
    i += 1