
#打印1-10使用while循环
# num = 1
# while num <= 10:
#     print(num)
#     num = num + 1

#打印1-10使用for循环
# for i in range(1,11):
#     print(i)

#打印2 4 6 8 10
# for i in range(2,12,2):  #第三个参数叫步长
#     print(i)

#打印从10到1的while版本
# num = 10
# while num >= 1:
#     print(num)
#     num = num - 1

#打印从10到1的for版本
# for i in range(10,0,-1):  #步长是按照-1的方式进行
#     print(i)

#求1+2+...+100的和
theSum = 0
for i in range(1,101):
    theSum += i
    print(theSum)