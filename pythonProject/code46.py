# 直接使用for循环遍历字典
a = {
    'id': 1,
    'name': 'zhangsan',
    'score': 90
}
for key in a:
    print(key, a[key])

# print(a.keys())
# print(a.values())
# print(a.items())

for key, value in a.items():
    print(key, value)