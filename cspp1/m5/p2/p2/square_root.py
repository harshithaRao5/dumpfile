"'#finding the square root of the given number'"
SQUARE = int(input())
i = 0.1
GUESS = 0
j = 0.1
while abs(GUESS**2 - SQUARE) >= i and GUESS <= SQUARE:
    GUESS += j
if abs(GUESS**2 - SQUARE) >= i:
    print('Failed on square root of', SQUARE)
else:
    print(str(GUESS))
