'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    #list_1 = []
    '''lines = int(input())
    for i in range(lines):
        input_1 = input()
        input_1 = split('\n')'''

        #list_1.append(input().split('/n'))
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(string)

if __name__ == '__main__':
    main()
