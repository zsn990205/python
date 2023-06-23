
# 这种情况不算有多个返回值
# def test():
#     return 1
#     return 2

def isOdd(num):
    """用来判定num是不是奇数 如果是奇数返回true"""
    if num % 2 == 1:
        return True
    else:
        return False


print(isOdd(9))
print(isOdd(10))

# 多元赋值
def getPoint():
    x = 10
    y = 20
    return x, y

x, y = getPoint()
print(x, y)