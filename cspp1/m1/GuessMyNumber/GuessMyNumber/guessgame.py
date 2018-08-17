"'#program for the guessgame'"
print("please think of a number between 0 to 100!")
LOW = 0
HIGH = 100
ANS = int((HIGH+LOW)/2)
print("is this your secret number :"+ str(ANS))
NUM = input("Enter 'h' for high. Enter 'l' for low Enter 'c' for correct:")
while NUM != 'c':
    if NUM == 'h':
        HIGH = ANS
        ANS = int((HIGH+LOW)/2)
        print("is this your secret number:"+ str(ANS))
        NUM = input("Enter 'h' for high. Enter 'l' for low Enter 'c' for correct:")
    if NUM == 'l':
        LOW = ANS
        ANS = int((HIGH+LOW)/2)
        print("is this your secret number:"+ str(ANS))
        NUM = input("Enter 'h' for high. Enter 'l' for low Enter 'c' for correct:")
    else:
        print("sorry i did not understand the input")
        print("is this your secret number:"+ str(ANS))
        NUM = input("Enter 'h' for high. Enter 'l' for low Enter 'c' for correct:")
if NUM == 'c':
    print("Enter 'h' for high. Enter 'l' for low Enter 'c' for correct:")
    print("Game over your secret number is:"+ str(ANS))
