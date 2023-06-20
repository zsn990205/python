

# 先定义一个求和函数
def calc_sum(beg, end):
    theSum = 0
    for i in range(beg, end+1):
        theSum += i
    print(theSum)


# 调用函数
calc_sum(1,100)
calc_sum(300,400)
calc_sum(1,1000)