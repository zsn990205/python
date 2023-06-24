

x = 10
def test():
    x = 20
    print(f'函数内部{x}')


test()
print(f'函数外部{x}')