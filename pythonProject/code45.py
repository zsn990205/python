# 1.在字典中新增元素,使用[]进行
a = {
    'id': 1,
    'name': 'zhangsan'
}

# 在字典里加上新的键值对,这是写操作
a['score'] = 90
print(a)

# 2.在字典中根据key修改value,也是使用[]进行的
a['score'] = 100
print(a)

# 3.使用pop方法根据key删除键值对
a.pop('name')
print(a)