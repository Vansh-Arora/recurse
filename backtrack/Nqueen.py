count = 0
def isSafe(A,N,r,c):
    # cHECK IF ANY QUEEN IS PRESENT IN THIS COLUMN
    for i in range(r):
        if A[i][c] == 1:
            return False
    # cHECK IF ANY QUEEN IS PRESENT IN THIS ROW
    for j in range(c):
        if A[r][j] == 1:
            return False
    # Check left diagonal
    i = r-1
    j = c-1
    while i >= 0 and j >= 0:
        if A[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check right diagonal
    i = r-1
    j = c+1
    while i >= 0 and j < N:
        if A[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True
    
def nQueen(A, N, r):
    global count
    if r == N:
        count +=1
        return
    for c in range(N):
        if isSafe(A, N, r, c):
            A[r][c] = 1
            nQueen(A,N,r+1)
            A[r][c] = 0

def createGrid(n):
    grid = []
    for i in range(n):
        grid.append([])
        for j in range(n):
            grid[i].append(0)
    return grid
A = createGrid(4)
nQueen(A,4,0)
print(count)

