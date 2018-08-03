"'#finding the square root of number using bisection method'"
X = int(input())
i = 0.1
Low = 0
High = X
Ans = (High + Low)/2.0
while abs(Ans**2 - X) >= i:
    if Ans**2 < X:
        Low = Ans
    else:
        High = Ans
    Ans = (High + Low)/2.0
print(str(Ans))


