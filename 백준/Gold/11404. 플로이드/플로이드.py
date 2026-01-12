import sys
input = sys.stdin.readline

INF = float("inf")
n = int(input())
m = int(input())
grp = [[INF] * (n+1) for _ in range (n+1)]

for k in range (1, n+1):
    grp[k][k] = 0

for i in range (0, m):
    a, b, c = map(int, input().split())
    grp[a][b] = min(grp[a][b], c)

for k in range (1, n+1):
    for s in range (1, n+1):
        for e in range (1, n+1):
            grp[s][e] = min(grp[s][k] + grp[k][e], grp[s][e])

for k in range (1, n+1):
    for s in range (1, n+1):
        print(0 if grp[k][s] == INF else grp[k][s], end=" ")
    print()