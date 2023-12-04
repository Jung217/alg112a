# 方法 1
def power2n_0(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_1(n):
    if n==0 or n==1: return n+1
    return power2n_1(n-1)+power2n_1(n-1)

# 方法 2b：用遞迴
def power2n_2(n):
    if n==0 or n==1: return n+1
    return 2*power2n_2(n-1)

# 方法 3：用遞迴+查表
def power2n_3(n):
    pow2 = [None]*1000
    pow2[0] = 1
    pow2[1] = 2
    if pow2[n] == None: return power2n_3(n-1)+power2n_3(n-1)
    else: return pow2[n]

n = int(input('Enter n : '))
print(f'power2n_0({n}) = {power2n_0(n)}')
print(f'power2n_1({n}) = {power2n_1(n)}')
print(f'power2n_2({n}) = {power2n_2(n)}')
print(f'power2n_3({n}) = {power2n_3(n)}')