"'#finding the perfect cube'"
CUBE = int(input())
GUESS = 0
for GUESS in range(abs(CUBE)+1):
    if GUESS**3 >= abs(CUBE):
        break
if GUESS**3 != abs(CUBE):
    print(str(CUBE)+ "is not a perfect cube")
else:
    if CUBE < 0:
        GUESS = -GUESS
    print(str(CUBE)+ " is a perfect cube")
