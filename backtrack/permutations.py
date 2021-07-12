def permute(str, j):
    if j == len(str) - 1:
        print(str)
        return
    for i in range(j,len(str)):
        str[i],str[j] = str[j],str[i]
        permute(str, j+1)
        str[i],str[j] = str[j],str[i]

permute(['A','B','C'],0)
