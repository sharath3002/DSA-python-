def anagram(str1,str2):
    str1=sorted(str1)
    str2=sorted(str2)
    if str1==str2:
        return "Anagram"
    else:
        return "Not an anagram"
str1=input("Enter the str1: ").strip()
str2=input("Enter the str2: ").strip()
print(anagram(str1,str2))



# ✅ Example:
# "listen" and "silent" are anagrams.

# "triangle" and "integral" are also anagrams.


def anagram(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    if sorted(str1)== sorted(str2):
        return "Anagram"
    else:
        return "Not an anagram"
str1=input("Enter str1 : ").strip()
str2=input("Enter str2 : ").strip()

print(anagram(str1,str2))