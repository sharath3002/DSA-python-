# Write a program to find a substring within a string. If found display its starting position

def find_substring(main_string, sub_string):
    
    position = main_string.find(sub_string)
    
    if position != -1:
        print(f"Substring found at position {position}")
    else:
        print("Substring not found")

# Input
main_string = input("Enter the main string: ").strip()
sub_string = input("Enter the substring to search: ").strip()

# Function call
find_substring(main_string, sub_string)



def substring(str1,str2):
    position=str1.find(str2)
    if position!=-1:
        print("Substring of str1")
        return  position
    else:
        return "Not a substring of str1"
str1=input("Enter str1 : ")
str2=input("Enter str2  : ")
print(substring(str1,str2))