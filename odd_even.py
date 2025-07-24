#to count odd and even numbers


# def odd_even(arr):
#     even_no=sum(1 for num in arr if num%2==0)
#     odd_no=len(arr)-even_no
    
#     print("Even numbers count :",even_no)
#     print("Odd numbers count :",odd_no)
    
# arr=[45,89,78,64,12,35,42,20,38]
# odd_even(arr)



def odd_even(arr):
    even_no=0
    odd_no=0
    for num in arr:
        if num%2==0:
            even_no+=1
        else:
            odd_no+=1
    return {"odd_no":odd_no,"even_no":even_no}
arr=[21,54,87,98,46,25,34,21,20,25,28]
print(odd_even(arr))


def odd_even(arr):
    even_no=sum(1 for num in arr if num%2==0)
    odd_no=len(arr)-even_no
    
    print("odd no: ",odd_no)
    print("even no: ",even_no)
    
arr=[45,54,87,98,46,25,34,21,20,25,28]
odd_even(arr)