

def add(x, y, debug=False):
    if debug:
        print(f'x = {x} y = {y}')
    return x + y


ret = add(10, 20)
print(ret)