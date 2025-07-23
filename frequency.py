def count_freq(arr):
    if len(arr)<1:
        return None
    freq={}
    for num in arr:
        freq[num]=freq.get(num,1)+1
    return freq

arr=[10,20,5,5,5,5,5,5,5,5,20,30,10,20,20,20,20]
print(count_freq(arr))


def duplicate(arr):
    freq={}
    duplicate=set()
    
    for num in arr:
        if num in freq:
            duplicate.add(num)
        
    return duplicate

arr=[1,2,3,1,2,3,1,2,3,0]
print(duplicate(arr))