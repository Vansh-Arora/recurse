def lexico(i,n):
    if i > n:
        return
    print(i)
    if i == 0: x = 1
    else: x = 0
    for j in range(x,10):
        lexico(i*10+j,n)
    
lexico(0,102)