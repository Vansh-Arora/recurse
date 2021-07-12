def Print(n):
    if n == 0:
        return
    Print(n-1)
    for i in range(n):
        print('*',end = '')
    print()

Print(3)

def pattern(n, i):
    if n == 0:
        return
    if i == 0:
        pattern(n-1,0)
    if i < n:
        print('*',end='')
        pattern(n,i+1)
    if i == n:
        print()
        return
pattern(3,0)

def Printer(n,i):
    if n == 0:
        return
    if i < n:
        print('*',end='')
        Printer(n,i+1)
    else:
        print()
        Printer(n-1,0)
Printer(3,0)