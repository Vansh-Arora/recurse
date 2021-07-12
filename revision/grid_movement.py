# m rows i
# n cols j
def move(m, n, i, j, ans):
    if i >= m or j >= n:
        return
    if i == m-1 and j == n-1:
        print(ans)
        return
    move(m,n,i+1,j,ans+'D ')
    move(m,n,i,j+1,ans+'R ')
    
def paths(m, n):
    move(m,n,0,0,'')

paths(2,2)