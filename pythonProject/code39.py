
# 1.使用in来看某个元素是否在列表中存在
a = [1, 2, 3, 4]
# in元素是针对整个列表进行遍历 但是不需要我们显示的写出
print(1 in a)
print(10 in a)
print(10 not in a)
print(1 not in a)
print('---------------')

# 2.使用index方法判断当前元素在列表中是否存在,返回的是元素的下标
a = [1, 2, 3, 4]
# 判断2这个元素是否在列表中存在,返回的也就是1
print(a.index(2))
# print(a.index(10))    不存在的时候抛出异常->xxx不在列表中