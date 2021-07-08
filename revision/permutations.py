def permute(str,perm):
    if len(str) == 0:
        print(perm)
        return
    
    for i in range(len(str)):
        permute(str[:i]+str[i+1:],perm+str[i])  ## Perm is not updated for current loop, a new copy is sent to each call
permute(['A','B','C'],'')