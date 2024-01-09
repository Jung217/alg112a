import random

def hillClimbing(f, init, h=0.01):
    p = init
    failCount = 0
    while failCount < 10000:
        fnow = f(p)
        p1 = p[0] + random.uniform(-h, h)
        f1 = f(p1)
        #p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:
            fnow = f1
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount += 1
        #if abs(fnow) < 0.001: break
    return p, fnow

#def neighbor(f, p, h=0.01):
#    p1 = p[0] + random.uniform(-h, h)
#    f1 = f([p1])
#    return [p1], f1

def f(x):
    return -1 * (x[0]**5 + 1)

print('\n', hillClimbing(f, [0.0]))