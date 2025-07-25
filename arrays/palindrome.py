
def Palindrome(s):#❌ Problem:
    s=s.lower()
    if s==s[::-1]:
        return True
    else:
        return False
s=input("Enter the string:").strip(':", ')
print(Palindrome(s))

#✅
def Palindrome(s):
    # Remove non-alphanumeric and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

s = input("Enter the string: ")
print(Palindrome(s))






def Palindrome(s):
    new=''.join(char.lower() for char in s if char.isalnum())
    if new==new[::-1]:
        return True
s=["A man, a plan, a canal: Panama"]
print(Palindrome(s))
