n=int(input())
low=1
high=n+1
for i in range(low,high,1):
    if(i%3==0 and i%5==0):
        i=print('Fizz')
        i='Buzz'    
    if(i%3==0):
        i='Fizz'
    elif(i%5==0):
        i='Buzz'
    
    print(i)
