'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
import re
def tokenize(string):
    adict = {}
    reg = re.compile('[^a-z]')
    string_1 = [reg.sub("", string_1.strip()) for string_1 in string.lower().split(" ")]
    for word in string_1:
        adict[word] = (string_1.count(word))
    return adict
def main():
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'  
    print(tokenize(string))
    

if __name__ == '__main__':
    main()
