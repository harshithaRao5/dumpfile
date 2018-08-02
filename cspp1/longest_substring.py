"'#finding the longest substring'"
S = input()
i = S[0]
j = ''
"'#checking for the string present in range'"
for a in range(1,len(S)):
    if S[a] >= i[len(i)-1]:
        i += S[a]
    else:
        if len(i) > len(j):
            j = i
    
        i=S[a]
        
if len(i)> len(j):
    j=i
print (j)
