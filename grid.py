def grid(m,n,i,j,ans):
    if i >=m or j >= n:
        return
    if i == m-1 and j == n-1:
        print(ans)
        return
    grid(m,n,i+1,j,ans+'D')
    grid(m,n,i,j+1,ans+'R')
    grid(m,n,i+1,j+1,ans+'->')

grid(3,3,0,0,'')