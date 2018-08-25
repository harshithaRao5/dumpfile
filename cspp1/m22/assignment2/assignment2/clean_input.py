'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''
def clean_string(string):
    '''sub function for cleaning the input'''
    clean_input = ''
    for i in string:
        if i not in "!@#$%^&*()_+-=}{][:;><.,/? ":
            clean_input = clean_input + i
    return clean_input

def main():
    '''main function'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
