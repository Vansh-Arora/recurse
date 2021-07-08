def permute(arr, beg):
    if beg == len(arr) - 1:
        print(arr)
        return
    for i in range(beg,len(arr)):
        arr[i],arr[beg] = arr[beg],arr[i]
        permute(arr, beg+1)
        arr[i],arr[beg] = arr[beg],arr[i]

permute(['V','A','N','S','H'],0)