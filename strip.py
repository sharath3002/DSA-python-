# ✅ .strip() in Python
# The .strip() method is used with strings to remove leading and trailing whitespace (spaces, tabs, newlines, etc.).

s="      hello world"
print(s.strip())

s = "\n\t  python\n"
print(s.strip())

s = "xxxHelloxx"
print(s.strip('x'))  # Removes 'x' from both ends

s = "xxxHelloxx"
print(s[3:8]) 


fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)
