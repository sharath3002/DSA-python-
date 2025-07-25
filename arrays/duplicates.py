

def Duplicates(arr):
    freq={}
    duplicate=[]
    for num in arr:
        freq[num]=freq.get(num,0)+1
    for key,value in freq.items():
        if value>1:
            duplicate.append(key)
    # if not duplicate:                      #this line return -1 if there was no duplicates so I removed this
    #     duplicate.append(-1)
    return duplicate
arr=[1,2,3,4,5,6,7,8,9]
print(Duplicates(arr))



























# Python code to find duplicates in an array
# using hashmap

def Duplicates(arr):

    # Step 1: Create an empty dictionary
    # to store element frequencies
    freq = {}
    duplicate = []

    # Step 2: Iterate through the array and
    # count element frequencies
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Step 3: Iterate through the dictionary to
    # find duplicates
    for key, value in freq.items():
        if value > 1:
            duplicate.append(key)


    if not duplicate:
        duplicate.append(-1)

    # Step 6: Return the result list containing
    # duplicate elements or -1
    return duplicate



arr = [1, 6, 5, 2, 3, 3, 2]
print(Duplicates(arr))




