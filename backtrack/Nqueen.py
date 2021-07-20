count = 0

def show(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:    print("- ",end='')
            else: print("Q ",end='')
        print()
    print('\n')
def isSafe(A,N,r,c):
    # cHECK IF ANY QUEEN IS PRESENT IN THIS COLUMN
    for i in range(r):
        if A[i][c] == 1:
            return False
    '''# cHECK IF ANY QUEEN IS PRESENT IN THIS ROW
    ## NOT REQUIRED
    for j in range(c):
        if A[r][j] == 1:
            return False'''
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
        show(A)
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
A = createGrid(5)
nQueen(A,5,0)
print(count)

