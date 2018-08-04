"'#printing the numbers 1 to n with replacements of fizz and buzz'"
N = int(input())
LOW = 1
HIGH = N + 1
for i in range(LOW, HIGH, 1):
    if(i%3 == 0 and i%5 == 0):
        i = print('Fizz')
        i = 'Buzz'
    elif i%3 == 0:
        i = 'Fizz'
    elif i%5 == 0:
        i = 'Buzz'
    print(i)
