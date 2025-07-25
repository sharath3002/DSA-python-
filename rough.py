
def Palindrome(s):
    new=''.join(char.lower() for char in s if char.isalnum())
    if new==new[::-1]:
        return True
s=["A man, a plan, a canal: Panama"]
print(Palindrome(s))
