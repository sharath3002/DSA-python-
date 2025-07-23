def descending(arr):
    if not arr:
        return None
    desc=sorted(arr,reverse=True)
    return desc
arr=[7,2,9,6,8,44]
print(descending(arr))