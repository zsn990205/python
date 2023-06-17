

#假设我要吃5个包子,第三个有虫跳过第三个不吃
# for i in range(1,6):
#     if i == 3:
#     #第三个包子有个虫
#         continue
#     print(f'我在吃第{i}个包子')

#吃5个包子
# for i in range(1,6):
#     if i == 3:
#     #第三个有虫我就不吃了
#         break
#     print(f'我在吃第{i}个包子')

#给定若干个数字,求平均值(不知道有几个数字的情况下)
#表示加和的结果
theSum = 0
#表示元素个数
count = 0
while True:
    num = input('请输入一个数字(;表示输入结束): ')
    #当用户输入;的时候表示输入结束
    if num == ';':
        break
    num = float(num)
    theSum += num
    count += 1
print(f'平均值是{theSum / count}')