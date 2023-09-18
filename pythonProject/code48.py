
# # 使用open打开文件
# f = open('E:/Python环境/test.txt', 'r')  # f->file
#
# print(f)
# print(type(f))
#
# # 关闭文件
# f.close()

# 打开文件个数的上限
fList = []
count = 0
while True:
    f = open('E:/Python环境/test.txt', 'r')
    fList.append(f)
    # f.close()
    count += 1
    f.close()
    print(f'打开文件的个数是: {count}')

# 使用write实现写文件
f = open('E:/Python环境/test.txt', 'w')
f.write('hello')
f.close()

