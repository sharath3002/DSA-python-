def MinMax(arr):
    n=len(arr)
    if (n%2==0):
        if arr[0]<arr[1]:
            min_no=arr[0]
            max_no=arr[1]
        else:
            max_no=arr[0]
            min_no=arr[1]
        i=2  #starting index for even no of arrays
    else:
        min_no=max_no=arr[0]
        i=1  # starting index for odd no of arrays
    while(i<n-1):
        if arr[i]<arr[i+1]:
            min_no=min(min_no,arr[i])
            max_no=max(max_no,arr[i+1])
        else:
            min_no=min(min_no,arr[i+1])
            max_no=max(max_no,arr[i])
        i+=2
    return {"Minimum":min_no,"Maximum":max_no}
arr=[89,78,56,2,20,3,45]
print(MinMax(arr))