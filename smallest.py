def smallest(arr):
    if not arr:
        return None
    smallest=arr[0]
    for num in arr:
        if num < smallest:
            smallest= num
    return smallest
s=input("Enter numbers : ")
arr=list(s)


print(smallest(arr))