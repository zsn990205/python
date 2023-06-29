# 写一个函数来求n的阶乘

# n! = n*(n-1)!
# 1! = 1
def factor(n):
    if n == 1:
        return n
    return n * factor(n-1)


print(factor(5))