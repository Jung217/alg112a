def truthtable(n, Curtable=[]):
    if n == 0:
        print(Curtable) 
        print("\n")
    else:
        for value in [0, 1]:
            print(Curtable)
            truthtable(n - 1, Curtable + [value])

truthtable(3)