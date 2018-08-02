"'#number of bob present in the given string'"
S = input()
COUNT = 0
LENGTH = int(len(S))
A = 0
B = 3
"'#checking that the limit doen't extend the length of the given string'"
while B <= LENGTH:
    Z = S[A:B]
    if Z == 'bob':
        COUNT = COUNT + 1
    A = A + 1
    B = B + 1
print(COUNT)
