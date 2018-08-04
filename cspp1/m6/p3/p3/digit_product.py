n=int(input())
r=0
c=1
i=0
while i<=n:
    r=n%10
    c=c*r
    n=n//10
    i=i+1
print(str(c))
