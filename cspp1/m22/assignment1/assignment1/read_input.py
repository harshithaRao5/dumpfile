'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''main function
    '''
    input_1 = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        input_1 += input()
        input_1 += '\n'
    print(input_1)

if __name__ == '__main__':
    main()
