import sys
from collections import deque
sys.setrecursionlimit(10**6)

def dfs(v):
    print(v, end=" ")
    visited[v] = True
    for node in grp[v]:
        if (visited[node] == False):
            dfs(node)

def bfs(v):
    que = deque()
    que.append(v)
    visited[v] = True
    while(que):
        t = que.popleft()
        print(t, end = " ")
        for node in grp[t]:
            if(visited[node] == False):
                que.append(node)
                visited[node] = True

n, m, v = map(int, input().split())
grp = [[] for _ in range (n+1)]

for _ in range (m):
    a, b = map(int, input().split())
    grp[a].append(b)
    grp[b].append(a)

for i in range (n+1):
    grp[i].sort()

visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)