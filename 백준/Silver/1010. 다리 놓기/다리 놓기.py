t = int(input())
a = [[0] * 31 for _ in range (31)]

for i in range (31):
    a[i][1] = i
    
for i in range (2, 31):
    for j in range (2, 31):
        a[i][j] = a[i-1][j] + a[i-1][j-1]

for _ in range (t):
    n, m = map(int, input().split())
    print(a[m][n])