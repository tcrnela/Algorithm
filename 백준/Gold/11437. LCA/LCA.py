import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global par, dep
    que = deque()
    que.append(1)
    vis[1] = True
    dep[1] = 1
    while(que):
        t = que.popleft()
        for node in arr[t]:
            if (vis[node] == False):
                dep[node] = dep[t] + 1
                par[node] = t
                que.append(node)
                vis[node] = True

def find(a, b):
    ans = 1
    while (dep[a] != dep[b]):
        if (dep[a] > dep[b]):
            a = par[a]
        else:
            b = par[b]

    if (a == b):
        print(a)
    elif (par[a] == par[b]):
        print(par[a])

    else:
        while(a != b):
            a = par[a]
            b = par[b]
        print(a)

n = int(input())
arr = [[] for _ in range (n+1)]
par = [0] * (n+1)
dep = [0] * (n+1)
vis = [False] * (n+1)
for _ in range (n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
bfs()
m = int(input())
for _ in range (m):
    a, b = map(int, input().split())
    find (a, b)