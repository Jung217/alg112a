# 原創

def truthtable(n, Curtable=[]):
    if n == 0:
        print(Curtable) 
    else:
        for value in [0, 1]:
            truthtable(n - 1, Curtable + [value])

for i in range(2):
    truthtable(i+2)
    print()