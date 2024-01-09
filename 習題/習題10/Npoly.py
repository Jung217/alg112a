import random

def hillClimbing(f, init, h=0.01):
    p = init
    failCount = 0
    while failCount < 10000:
        fnow = f(p)
        neighbor = p.copy()

        for i in range(len(neighbor)): neighbor[i] += random.uniform(-h, h)
        f1 = f(neighbor)

        if f1 < fnow:
            if f1 <= 0 : break
            fnow = f1
            p = neighbor.copy()
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount += 1
        
        if fnow < 0.001: break
    return p, fnow

def f(x):
    return x[0]**5 + 1

print('\n', hillClimbing(f, [0.0]))