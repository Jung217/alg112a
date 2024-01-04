# 原創

fib = [None]*1000
fib[0] = fib[1] = 1
n = int(input("Enter n : "))

if n==0:
    print(f'fibonacci({n}) = {0}')
else:
    for i in range(n-2):
        tn = 2 + i  # 從2開始
        fib[tn] = fib[tn-1] + fib[tn-2]
    print(f'fibonacci({n}) = {fib[n-1]}')