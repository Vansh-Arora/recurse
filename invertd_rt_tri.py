def pattern(n,i):
    if n == 0:
        return
    if i < n:
        print('*',end='')
        pattern(n,i+1)
    else:
        print()
        pattern(n-1,0)

pattern(4,0)