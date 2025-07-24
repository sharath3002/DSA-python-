


    
def palindrome(a):
    a=a.lower()
    reversed_a=a[::-1]
    if a==reversed_a:
        return "Palindrome"
    else:
        return "Not a Palindrome"
a="MalaYalam"
print(palindrome(a))




def palindrome(S):
    if S == S[::-1]:
        print("YES")
    else:
        print("NO")
    
S=input().strip()
palindrome(S)   # X print is not used 


#     Your current code works correctly in checking whether a string is a palindrome, but there's a small issue: you're using print(palindrome(S)), which prints None after the actual result because the palindrome() function itself already prints the result but doesn’t return anything.
