n = int(input())
a = []
dp = [[0] * n for _ in range (n)]

for i in range (n):
    t = list(map(int, input().split()))
    a.append(t)

for i in range (1, n):
    for j in range (len(a[i])):
        if j == 0:
            a[i][j] += a[i-1][j]
        elif j == len(a[i]) - 1:
            a[i][j] += a[i-1][j-1]
        else:
            a[i][j] += max(a[i-1][j-1], a[i-1][j])

print(max(a[n-1]))