passengers = 0
ans1 = []
def move(A,m, n, i, j, ans):
    global passengers
    global ans1
    if i >= m or j >= n or A[i][j]== -1:
        return
    if i == m-1 and j == n-1:
        ans1.append(passengers)
        passengers = 0
        print(ans)
        return
    if A[i][j] == 1:
        passengers += 1
        A[i][j] = 2
    move(A,m,n,i+1,j,ans+'D ')
    move(A,m,n,i,j+1,ans+'R ')
    
    if A[i][j] ==2:
        A[i][j] = 1
        return
A = [[0,1],[0,1]]    
def paths(A,m, n):
    move(A,m,n,0,0,'')

paths(A,2,2)
print(ans1)