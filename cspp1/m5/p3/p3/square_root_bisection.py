"'#finding the square root of number using bisection method'"
X = int(input())
i = 0.01
LOW = 0
HIGH = X
ANS = (HIGH + LOW)/2.0
while abs(ANS**2 - X) >= i:
    if ANS**2 < X:
        LOW = ANS
    else:
        HIGH = ANS
    ANS = (HIGH + LOW)/2.0
print(ANS)
