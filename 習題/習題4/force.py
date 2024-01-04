# 參考老師上課範例

# x^2 - 3x + 1 = 0
from numpy import arange
import math

def f(x) :
    return x**2/3 - x + 1/3
    #return math.sin(x*x+2*x)/x*x*x 

for x in arange(-100, 100, 0.001):
    if abs(f(x)) < 0.001:
        print("x=", x, " f(x)=", f(x)) 