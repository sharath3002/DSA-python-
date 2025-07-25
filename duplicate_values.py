#this code prints the duplicate values as well as array values

def duplicate_values(arr):
    freq={}
    duplicate=set()
    for num in arr:
        duplicate.add(num)
    freq[num]=freq.get(num,0)+1
    return duplicate

arr=[1,2,3,4,2,1,2,3,4,5,6]
print(duplicate_values(arr))
