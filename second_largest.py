def second_largest(arr):
    if len(arr)<2:
        return None
    first= second= float('-inf')
    
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first>num>second:
            second=num
    return second if second!=float('-inf') else None

arr=[-5,7,-9,8,-58,85]
print(second_largest(arr))



# 🔍 Without float('-inf'), let’s say you do:

# first = second = 0 since zero is greater than the negative numbers so first it checks for 0 in this case else -inf
# Then it fails if your list only contains negative numbers, like:


# arr = [-5, -2, -10]
# Here, all numbers are less than 0, so the loop never updates first or second, and you'll get incorrect results.

# ✅ Using float('-inf') handles:
# Negative numbers

# Mixed values (positive/negative)

# Edge cases like duplicates


def second_largest(arr):
    if len(arr)<2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num> first:
            second = first
            first = num
        elif first>num>second:
            second=num
    return second if second!= float('-inf') else None

arr=[5,8,9,6,7]
print(second_largest(arr))