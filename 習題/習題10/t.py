import random

def hillClimbing(f, p, h=0.01):
    failCount = 0
    while failCount < 10000:
        fnow = f(p)
        fneighbor = p.copy()
        for i in range(len(fneighbor)):
            fneighbor[i] += random.choice([-h, h, 0])
        fneighbornow = f(fneighbor)

        if fneighbornow < fnow:
            p = fneighbor.copy()
            print('p=', p, 'f(p)=', f(p))
            failCount = 0
        else:
            failCount = failCount + 1

        if fnow < 0.001:
            break

    return p, fnow

def f1(p):
    return p[0] ** 5 + 1

hillClimbing(f1, [0])