
# 1.使用append往列表末尾来新增元素
a = [1, 2, 3, 4]
a.append(5)
a.append('hello')
print(a)

# 表示针对哪个对象进行展开的
b = [5, 6, 7, 8]
b.append('world')
print(b)

print('----------------------------')

# 2.还可以使用insert方法,往列表中别的位置来新增元素
a = [1, 2, 3, 4]
a.insert(1, 'hello')
# 当插入的元素超过列表长度进行插入时
a.insert(100,'hello')
print(a)