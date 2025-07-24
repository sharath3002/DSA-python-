def vowel_consonant(str):
    vowels="AEIOUaeiou"
    vowel_count=0
    consonant_count=0
    for char in str:
        if char in vowels:
            vowel_count+=1
        else:
            consonant_count+=1
    return {vowel_count,consonant_count}
str="sharathmhhiriyappa"
print(vowel_consonant(str))



def vowel_consonant(str):
    vowels="aAeEiIoOuU"
    vowel_count=sum(1 for char in str if char in vowels)
    consonant_count=sum(1 for char in str if char.isalpha() and char not in vowels)
    
    print("Vowels count: ",vowel_count)
    print("Consonant Count :",consonant_count)
str="delllaptop"
vowel_consonant(str)