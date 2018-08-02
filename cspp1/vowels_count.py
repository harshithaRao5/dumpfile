"'#taking the input string'"
S = input("enter the string")
COUNT = 0
"'#checking the range of the strings'"
for vowel in S:
    if vowel in 'aeiou':
        COUNT = COUNT+1

print("number of vowels:", COUNT)
