def second_smallest(arr):
    if len(arr)<2:
        return None
    first = second= float('inf')
    for num in arr:
        if num < first:
            second= first
            first = num
            
        elif first<num<second:
            second= num
            
    return second if second !=float('inf') else None
arr=[5,8,0,1,5]
print(second_smallest(arr))

# You initialized with float('-inf'), which is for maximum-finding, not minimum.

# For finding the smallest, you need to start with positive infinity: float('inf').