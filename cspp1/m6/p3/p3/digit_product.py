"'#given a number multiplying the digits of the number'"
N = int(input())
R = 0
C = 1
i = 0
NF = 1
if(N <= 0):
	NF = -1
	N = -N
while i <= abs(N):
    R = N % 10
    C = C * R
    N = N // 10
    i = i + 1
print(str(NF*C))
