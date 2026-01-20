import sys
import math
from collections import deque
input = sys.stdin.readline

def find(a, b, n):
    df = abs(dep[a] - dep[b])

    for k in range (n, -1, -1):
        if 2**k <= df:
            if (dep[a] < dep[b]):
                b = par[k][b]
                df -= 2**k
            elif (dep[a] > dep[b]):
                a = par[k][a]
                df -= 2**k

    if (a == b):
        print(a)
        return
    
    n = int(math.log2(dep[a]))
    for k in range (n, -1, -1):
        if par[k][a] != par[k][b]:
            a = par[k][a]
            b = par[k][b]

    if (a == b):
        print(a)
    else:
        print(par[0][a])

n = int(input())
k = int(math.log2(n))
grp = [[] for _ in range (n+1)]
vis = [False] * (n+1)
par = [[0] * (n+1) for _ in range (k+1)]
dep = [0] * (n+1)

for _ in range (n-1):
    a, b = map(int, input().split())
    grp[a].append(b)
    grp[b].append(a)

que = deque()
que.append(1)
vis[1] = True
dep[1] = 1
while(que):
    t = que.popleft()
    for node in grp[t]:
        if vis[node] == False:
            dep[node] = dep[t] + 1
            par[0][node] = t
            vis[node] = True
            que.append(node)

for i in range (1, k+1):
    for j in range (1, n+1):
        par[i][j] = par[i-1][par[i-1][j]]

m = int(input())
for _ in range (m):
    a, b = map(int, input().split())
    find(a, b, k)