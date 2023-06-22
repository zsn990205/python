
# 求beg end这个范围内的数字之和
def calcSum(beg, end):
    theSum = 0
    for i in range(beg, end+1):
        theSum += i
    return theSum


ret = calcSum(1, 100)
print(ret)

