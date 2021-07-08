# Base case 
    ## Print the array, if empty
# Recurse
    ## Find the sbuset for arr[i:]
# Self Work
    ## once Add ith element to the ans array
    ## once skip the ith element from answer
def sub(arr, n, i, ans):
    if i == n:
        print(ans)
        return
    sub(arr,n,i+1,ans+str(arr[i]) + ' ')
    sub(arr, n ,i+1, ans)


def subset(arr):
    sub(arr,len(arr),0,'')


subset([1,2,3])