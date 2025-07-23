


    
def palindrome(a):
    a=a.lower()
    reversed_a=a[::-1]
    if a==reversed_a:
        return "Palindrome"
    else:
        return "Not a Palindrome"
a="MalaYalam"
print(palindrome(a))