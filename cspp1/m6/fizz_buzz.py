n=int(input())
low=1
high=n+1
for i in range(low,high,1):
    if(i%3==0):
        if(i%5==0):
            i='FizzBuzz'
    if(i%3==0):
        i='fizz'
     
        
    elif(i%5==0):
        i='Buzz'
    
    
        
    print(i)
