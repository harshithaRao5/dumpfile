'''# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.
# This function takes in two arguments character and String and returns one boolean value.'''
def is_in(char, a_str):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    ans=len(a_str)//2
    if len(a_str)==1:
        if a_str[0]==char:
            return True
        else:
            return False
    if a_str[ans]==char:
            return True
    else:
        if a_str[ans]>char:
            return is_in(char, a_str[0:ans])
        else:
            return is_in(char, a_str[ans:len(a_str)])

    
def main():
    data = input()
    data = data.split()
    print(is_in((data[0][0]), data[1]))
if __name__== "__main__":
    main()
