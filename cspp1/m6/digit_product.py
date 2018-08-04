N = int(input())
R = 0
C = 1
i = 0
while i <= N:
    R = N % 10
    C = C * R
    N = N // 10
    i = i + 1
print(str(C))
