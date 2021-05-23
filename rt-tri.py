def pattern(n,i):
    if n == 0:
        return
    if i == 0:
        pattern(n-1,0)
    if i < n:
        print('*',end='')
        pattern(n,i+1)
    else:
        print()


pattern(4,0)