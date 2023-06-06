

# a = 10
# b = 20
# a = 'hello'
# b = 'world'
#
# print(a < b)
# print(a > b)
# print(a <= b)
# print(a >= b)
# print(a == b)
# print(a != b)

# print(0.1 + 0.2)
# print(0.1 + 0.2 == 0.3)

a = 0.1 + 0.2
b = 0.3
#这个代码是看a-b的差是否是一个非常小的数字,是否在误差内
print(-0.000001 < (a - b) < 0.000001)