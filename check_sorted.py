def check(arr,n,i):
    if n <= 1:
        return True
    if check(arr,n-1,i+1):
        if arr[i] <= arr[i+1]:
            return True
    else: return False

print(check([1,2,5,4],4,0))
