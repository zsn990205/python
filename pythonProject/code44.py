
# 1.使用in来判断某个key是否存在在字典中
a = {
    'id': 1,
    'name': '张三'
}
print('id' in a)
print('classId' in a)

# in只是判断key是否存在于字典中,无法判断value
print('张三' in a)
print('-----------------------')

# not in 判断key在字典中不存在
print('id' not in a)
print('classId' not in a)
print('-----------------------')

# 2.使用[]来根据key获取到value
a = {
    'id': 1,
    'name': '张三',
     100: '李四'
}
print(a['id'])
print(a['name'])
print(a[100])
# print(a['classId'])