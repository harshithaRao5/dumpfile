'''# Exercise: Assignment-1
# Write a Python function, factorial(n),takes number and returns the factorial of given number.
# This function takes in one number and returns one number.'''
def factorial(num):
    '''#sub function'''
    if num in (0, 1):
        return 1
    return num * factorial(num - 1)
def main():
    '''# main function'''
    ipt = input()
    print(factorial(int(ipt)))
if __name__ == "__main__":
    main()
