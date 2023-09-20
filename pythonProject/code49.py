
# 使用write实现写文件
f = open('E:/Python环境/test.txt', 'w')
f.write('hello')
f.close()

# 写文件的时候使用r方式打开
# f = open('E:/Python环境/test.txt', 'r')
# f.write('world')
# f.close()

# 写方式打开又有两种情况 直接写方式打开 追加写方式打开
f = open('E:/Python环境/test.txt', 'w')
f.write('1111\n')
f.close()

f = open('E:/Python环境/test.txt', 'a')
f.write('2222')
f.close()

# 如果文件对象已经被关闭
# 那么意味着系统中和文件相关的系统资源已经被释放
# 此时在强行去写 就会抛出异常
f = open('E:/Python环境/test.txt', 'w')
f.close()
# f.write('hello')