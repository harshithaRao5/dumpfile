"'#finding square of a number using newton rapson'"
i = 0.01
Y = int(input())
GUESS = Y/2.0
while abs(GUESS*GUESS - Y) >= i:
    GUESS = GUESS - (((GUESS**2) - Y)/(2*GUESS))
print(GUESS)
