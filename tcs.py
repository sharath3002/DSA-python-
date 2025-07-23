
# Contents


# 1. Problem on strays
# 2. Problem on Numbers
# 3. Problem on Number System
# 4. Problem on Sorting
# 5. Problem on Strings


# 1. Problems on strays
# Find the smallest number in an stray
# Find the largest number in an stray
# Second Smallest and Second Largest element in an stray
# Reverse a given stray
# Count frequency of each element in an stray
# Restrange stray in increasing-decreasing order
# Calculate sum of the elements of the stray
# Rotate stray by K elements - Block Swap Algorithm
# Average of all elements in an stray
# Find the median of the given stray
# Remove duplicates from a sorted stray
# Remove duplicates from unsorted stray
# Adding Element in an stray
# Find all repeating elements in an stray
# Find all non-repeating elements in an stray
# Find all symmetric pairs in stray
# Maximum product substray in an stray
# Replace each element of the stray by its rank in the stray
# Sorting elements of an stray by frequency
# Rotation of elements of stray- left and right
# Finding equilibrium index of an stray
# Finding Circular rotation of an stray by K positions
# Sort an stray according to the order defined by another stray
# Search an element in an stray
# Check if stray is a subset of another stray or not



# 2.Problems on Numbers
# Check if a number is palindrome or not
# Find all Palindrome numbers in a given range
# Check if a number is prime or not
# Prime numbers in a given range
# Check if a number is armstrong number of not
# Check if a number is perfect number
# Even or Odd
# Check weather a given number is positive or negative
# Sum of first N natural numbers
# Find Sum of AP Series
# Program to find sum of GP Series
# Greatest of two numbers
# Greatest of three numbers
# Leap Year or not
# Reverse digits of a number
# Maximum and Minimum digit in a number
# Print Fibonacci upto Nth Term
# Factorial of a number
# Power of a number
# Factors of a given number
# Print all prime factors of the given number
# Check if a number is a strong number or not
# Check if a Number is Automorphic
# GCD of two numbers
# LCM of two numbers
# Check if a number is Harshad number
# Check if the number is abundant number or not
# Sum of digits of a number
# Sum of numbers in the given range
# Permutations in which N people can occupy R seats in a classroom
# Program to add two fractions
# Replace all 0s with 1s in a given integer
# Can a number be expressed as a sum of two prime numbers
# Calculate the area of circle
# Program to find roots of a Quadratic Equation



# 3.Problems on Number System
# Convert Binary to Decimal
# Convert binary to octal
# Decimal to Binary conversion
# Convert decimal to octal
# Convert octal to binary
# Convert octal to decimal
# Convert digits/numbers to words



# 4.Problems on Sorting
# Bubble Sort Algorithm
# Selection Sort Algorithm
# Insertion Sort Algorithm
# Quick Sort Algorithm
# Merge sort algorithm



# 5.Problems on String
# Check if a given string is palindrome or not
# Count number of vowels, consonants, spaces in String
# Find the ASCII value of a character
# Remove all vowels from the string
# Remove spaces from a string
# Remove characters from a string except alphabets
# Reverse a String
# Remove brackets from an algebraic expression
# Sum of the numbers in a String
# Capitalize first and last character of each word
# Calculate frequency of characters in a string
# Find Non-repeating characters of a String
# Check if two strings are anagram of each other
# Count common sub-sequence in two strings
# Check if two strings match where one string contains wildcard characters
# Return maximum occurring character in the input string
# Remove all duplicates from the input string.
# Print all the duplicates in the input string.
# Remove characters from first string present in the second string
# Change every letter with the next lexicographic alphabet in the given string
# Write a program to find the largest word in a given string.
# Write a program to sort characters in a string
# Count number of words in a given string
# Write a program to find a word in a given string which has the highest number of repeated letters
# Change case of each character in a string
# Concatenate one string to another
# Write a program to find a substring within a string. If found display its starting position
# Reverse words in a string



# smallest element in an stray

# def find_smallest(str):
#     if not str:
#         return None
#     smallest = str[0]  # Assume first element is the smallest
#     for num in str:
#         if num < smallest:
#             smallest = num
#     return smallest

# # Example usage
# str = [5, 3, 9, 10, 7]
# print("Smallest element:", find_smallest(str))




# def min(str):
#     min = str[0]
#     for num in str:
#         if num<min:
#             min = num
#     return min

#     if not str:
#         return None

# # str=[10,3,4,5]
# # print("Smallest element in an stray is:",min(str))

# str = list(map(int, input("Enter numbers separated by space: ").split()))
# print("Smallest element:",min(str))


# str=[10,8,9]

# def min(str):
#     min=str[0]
#     for num in str:
#         if num<min:
#             num=min
#     return min

#     if not str:
#         return None

# print(min(str))


#largest element

# def largest_num(str):
#     largest=str[0]
#     for num in str:
#         if num>largest:
#             largest=num
#     return largest

#     if not str:
#         return None

# str=[5,4,7,8,100] 
# print(largest_num(str))
            
            
# reversing an stray

# str=[4,3,2,1]
# def reversed_stray(str):
#     reversed_str=str[::-1]
#     return reversed_str
# print(reversed_stray(str))



# str="malayalam"
# def reversed_string(str):
#     reversed_string=str[::-1]
#     return reversed_string
# print(reversed_string(str))


# smallest integer in a string

# string ="789256"
# def smallest_num(string):
    
    
    
#     if not string:
#         return None
#     smallest=string[0]

#     for num in string:
#         if num<smallest:
#             smallest=num
#     return smallest
        
# print("The smallest number is :",smallest_num(string))


# Given two integers N and E, where N represents the number of full water bottles and E represents the number of empty bottles that can be exchanged for a full water bottle. The task is to find the maximum number of water bottles that can be emptied. 

# Examples:


# Input: N = 9, E = 3
# Output: 13
# Explanation:
# Initially, there are 9 fully filled water bottles. 
# All of them are emptied to obtain 9 empty bottles. Therefore, count = 9
# Then exchange 3 bottles at a time for 1 fully filled bottle. 
# Therefore, 3 fully filled bottles are obtained. 
# Then those 3 bottles are emptied to get 3 empty bottles. Therefore, count = 9 + 3 = 12
# Then those 3 bottles are exchanged for 1 full bottle which is emptied. 
# Therefore, count = 9 + 3 + 1 = 13.


# second largest number

# def second_largest(arr):
#     if len(arr)<2:
#         return None
    
#     first = second = float('-inf')
#     for num in arr:
#         if num>first:
#             second = first
#             first = num
#         elif num>second and num != first:
#             second=num
#     return second if second != float('-inf') else None

# arr=[10,60,30,40]
# print(second_largest(arr))


# def second_largest(arr):
#     if len(arr)<2:
#         return None
    
#     first = second = float('-inf')
#     for num in arr:
#         if num>first:
#             second = first
#             first = num
#         elif num>second and num != first:
#             second=num
#     return second if second != float('-inf') else None

# str="145987"
# arr=[int(digit) for digit in str]
# print(second_largest(arr))



# def second_smallest(arr):
#     if len(arr)<2:
#         return None
    
#     first = second = float('inf')
#     for num in arr:
#         if num<first:
#             second = first
#             first = num
#         elif num<second and num != first:
#             second=num
#     return second if second != float('inf') else None
# # arr=[10,60,30,40]
# str="145987"
# arr=[int(digit) for digit in str]
# print(second_smallest(arr))



# def second_smallest(arr):
#     if len(arr)<2:
#         return None
#     first = second = float('inf')
#     for num in arr:
#         if num<first:
#             second=first
#             first=num
#         elif num<second and num!=first:
#             second = num
#     return second if second != float('inf') else None

# # arr=[10,20,30]
# str="789456"
# arr=[int(digit) for digit in str]
# print(second_smallest(arr))

# def second_largest(arr):
#     if len(arr)<2:
#         return None
#     first = second = float('-inf')
#     for num in arr:
#         if num>first:
#             second=first
#             first=num
#         elif num>second and num!=first:
#             second=num
            
#     return second if second!=float('-inf') else None

# arr=[10,50,80,170]
# print(second_largest(arr))

# count the frequency of an array


# def count_freq(arr):
#     freq={}
#     for num in arr:
#         freq[num]=freq.get(num,0)+1
#     return freq

# str="4444444"
# # arr=[4,4,4,4,4]
# arr=[int(digit) for digit in str]
# print(count_freq(arr))


# palindrome

# def palindrome(str):
#     str=str.lower()
#     reverse_str=str[::-1]
#     if reverse_str==str:
#         return "Palindrome"
#     else:
#         return "Not a Palindrome"
    

# str="Malayalam"
# print(palindrome(str))
# arr=list(str)
# print(arr)


# Ascending and Descending order

# def ascending(arr):
#     asc=sorted(arr)
#     return asc
# def descendig(arr):
#     desc=sorted(arr,reverse=True)
#     return desc

# arr=[56,89,48,72,12]
# print("Ascending order",ascending(arr))
# print("Descending order",descendig(arr))



# duplicate values

# def duplicate(arr):
#     freq={}
#     duplicate=set()
    
#     for num in arr:
#         if num in freq:
#             duplicate.add(num)
#         freq[num]=freq.get(num,0)+1
#     return duplicate

# arr=[1,2,3,1,2,3,1,2,3]
# print(duplicate(arr))




# str="12345"
# arr=list(str)

# print(arr)


# count the number of odd and even numbers in an array

# def odd_even(arr):
#     even_no=sum(1 for num in arr if num%2==0)
#     odd_no=len(arr)-even_no
    
#     print("Even numbers count :",even_no)
#     print("Odd numbers count :",odd_no)
    
# arr=[45,89,78,64,12,35,42,20,38]
# odd_even(arr)

# # even_no= sum(1 for num in arr if num%==0)



# vowel and consonant count in a string or word

def vowel_consonant(str):
    vowels="aAeEiIoOuU"
    vowel_count=sum(1 for char in str if char in vowels)
    consonant_count=sum(1 for char in str if char.isalpha() and char not in vowels)
    
    print("Vowels count: ",vowel_count)
    print("Consonant Count :",consonant_count)
str="delllaptop"
vowel_consonant(str)
    