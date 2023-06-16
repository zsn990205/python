

#使用while实现1-100的和
# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
# #在这儿注意一下 假如没有把print和while顶格写
# #则会导致打印出sum计算的每一次值
# print(f'sum={sum}')

#求1-5的阶乘
# num = 1
# ret = 1
# while num <= 5:
#     ret *= num
#     num += 1
# print(f'ret={ret}')

#求1!+2!+..+5!
num = 1
sum = 0
while num <= 5:
#先计算出当前的num的值是多少 往sum上进行累加
    ret = 1
    i = 1
    while i <= num:
      ret *= i
      i += 1
    sum += ret
    num += 1
print(sum)

