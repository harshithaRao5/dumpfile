'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    '''reg = re.compile('[^a-z A-Z 0-9]')
    clean_input = [reg.sub("", clean_input.strip()) for clean_input in string.split(" ")]
    return clean_input'''
    clean_input = ''
    for i in string:
        if i not in "!@#$%^&*()_+-=}{][:;><.,/? ":
            clean_input = clean_input + i
    return clean_input

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
