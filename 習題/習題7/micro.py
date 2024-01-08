#參考:https://github.com/ccc-py/micrograd/?tab=readme-ov-file#example-usage

from micrograd.engine import Value

a = Value(2.0)
b = Value(1.0)
c = Value(3.0)

for i in range(100000):
    step = 0.01
    f = a**2 + b**2 + c**2

    print('f(p) = {}, p = [{}, {}, {}]'.format(f.data, a.data, b.data, c.data))

    f.backward()
    if(a.grad < 0.001): break
    
    a -= a.grad * step
    b -= b.grad * step
    c -= c.grad * step
    
print('\nf(p) = {}, p = [{}, {}, {}]'.format(f.data, a.data, b.data, c.data))