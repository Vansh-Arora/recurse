from typing import Counter


count = 0
def show(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if A[i][j] == 0:    print("- ",end='')
            else: print("Q ",end='')
        print()
    print('\n')

def nQueen(A,n,r):
    global count
    if r == n:
        count += 1
        show(A)
        return
    for c in range(N):
        if isSafe(A,n,r,c):
            A[r][c] = 1
            nQueen(A,n,r+1)
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