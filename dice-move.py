def dice(n,i,ans):
    if i == n-1:
        print(ans)
        return
    if i > n-1:
        return
    for j in range(1,7):
        dice(n,i+j,ans+str(j))

dice(4,0,'') 