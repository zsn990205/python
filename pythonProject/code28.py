x = 10


# def test():
#     print(f'x = {x}')
#
#
# test()

# 修改全局变量
def test():
    global x
    x = 20

    
test()
print(f'x = {x}')