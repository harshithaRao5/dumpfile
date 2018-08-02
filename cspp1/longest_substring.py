S = input("enter string")
l = 0
i = S[0]
j = S[0]
for a in range(len(S) - 1):
    if S[a + 1] >= S[a]:
        i += S[a + 1]
        if len(i) > l:
            l= len(j)
            i = j
    else:
        i=S[a + 1]
        
    a += 1

print ('Longest substring in alphabetical order is: '  ,j)
