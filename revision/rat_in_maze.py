# To check if cell is visited and if cell is in the grid or not
def unvisited_ingrid(V,m,n,i,j):
    if i >=0 and j >= 0 and i < m and j < n and V[i][j] == 0:
        return 1
    else: return 0


def helper(M,V,m,n,i,j,ans):
    if i == m-1 and j == n-1:
        print(ans)
        return
    if not unvisited_ingrid(V,m,n,i,j):
        return
    # Mark current cell as visited
    V[i][j] = 1

    # Move Up
    if i > 0:
        helper(M,V,m,n,i-1,j,ans+'U')
    # Move Down
    if i < m-1:
        helper(M,V,m,n,i+1,j,ans+'D')
    # Move Left 
    if j > 0:
        helper(M,V,m,n,i,j-1,ans+'L')
    # Move right
    if j < n-1:
        helper(M,V,m,n,i,j+1,ans+'R')
    V[i][j] = 0
def Paths(M,m,n):
    V = []
    for i in range(m):
        V.append([])
        for j in range(n):
            V[i].append(0)
    
    helper(M,V,m,n,0,0,'')

Paths([[0, 0, 0], [0, 0, 0], [0, 0, 0]],3,3)