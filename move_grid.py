def move(m,n,i,j,osf):
    if i == m-1 and j == n-1:
        print(osf)
        return
    if i < m:
        move(m,n,i+1,j,osf+'d')
    if j < n:
        move(m,n,i,j+1,osf+'r')

move(3,3,0,0,'')