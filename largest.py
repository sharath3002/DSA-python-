def largest(arr):
    largest=arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest
arr=[45,78,96,104,156]
print(largest(arr))
    