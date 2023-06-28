
# def test():
#     print('hello')
#
#
# test()

#嵌套调用的层数有很多

def a():
    print('函数a')

def b():
    print('函数b')
    a()

def c():
    print('函数c')
    b()

def d():
    print('函数d')
    c()

d()