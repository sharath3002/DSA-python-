def duplicate_values(arr):
    freq={}
    duplicate=set()
    for num in arr:
        duplicate.add(num)
    freq[num]=freq.get(num,0)+1
    return duplicate

arr=[1,2,5,1,4,1,8,8,8,4,4,5,5,2,2,1,0,0,0,0]
print(duplicate_values(arr))