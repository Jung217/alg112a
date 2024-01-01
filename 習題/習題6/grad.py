# 參考老師上課範例
import numpy as np
from numpy.linalg import norm

# 偏微分
def df(f, p, k ,step=0.01):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

# 梯度下降
def gradDescendent(f, p0, step=0.01, max=100000, dp=10):
    p = p0.copy()
    fp0 = f(p)
    for i in range(max):
        fp = f(p)
        gp = grad(f, p) 
        glen = norm(gp) 
        if i % dp == 0: 
            print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp, str(p), str(gp), glen))
        if glen < 0.00001:
            break
        gstep = np.multiply(gp, -1*step) 
        p +=  gstep 
        fp0 = fp
    print('\n{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}\n'.format(i, fp, str(p), str(gp), glen))
    return p

def f(p):
    [x, y, z] = p
    return (x-5)**2+(y-1)**2+(z-3)**2

gradDescendent(f, [0.0, 0.0, 0.0])