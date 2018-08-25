'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    adict = {}
    string_1 = string.split()
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
