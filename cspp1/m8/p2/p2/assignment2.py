'''# Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in
# one number and returns the sum of digits of given number.
# This function takes in one number and returns one number.'''
def sum_of_digits(num):
    '''# sub function'''
    if num == 0:
        return 0
    return num % 10 + sum_of_digits(num // 10)
def main():
    '''# main function'''
    ipt = input()
    print(sum_of_digits(int(ipt)))
if __name__ == "__main__":
    main()
