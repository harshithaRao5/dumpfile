"'#taking the input string'"
S = input()
COUNT = 0
"'#checking the range of the strings'"
for vowel in S:
    if vowel in 'aeiou':
        COUNT = COUNT+1

print(COUNT)
