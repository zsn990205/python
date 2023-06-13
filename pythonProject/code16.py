

#(1)输入一个整数,判定是否是奇数
# num = input('请输入一个整数: ')
# #因为上述输入的是一个字符串类型的数字,所以需要强转
# num = int(num)
#
# if num % 2 == 0:
#     print('偶数')
# else:
#     print('奇数')

#(2)输入一个整数判断是正数还是负数
# num = int(input('请输入一个整数: '))
# if num > 0:
#     print('这个是正数')
# elif num < 0:
#     print('这是个负数')
# else:
#     print('这是个0')

#(3)判定一个年份是否是闰年
year = int(input('请输入一个年份: '))
# if year % 100 == 0:
#     if year % 400 == 0:
#         print('这是一个世纪闰年')
#     else:
#         print('这是一个平年')
# else:
#     if year % 4 == 0:
#         print('这是一个普通闰年')
#     else:
#         print('这是一个平年')

#以下是上面代码的精简版 前面表示普通闰年,后面则是世纪闰年.
if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
    print('闰年')
else:
    print('平年')