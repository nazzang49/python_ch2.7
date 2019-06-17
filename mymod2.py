import mymod

def power(x, y):
    r = 1
    for i in range(y):
        r = mymod.multiply(r, x)
    return r

print('모듈이름 : ' + __name__)
