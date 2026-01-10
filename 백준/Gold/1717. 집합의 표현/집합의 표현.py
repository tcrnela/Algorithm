import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    global par
    if (par[a] != a):
        par[a] = find(par[a])
    return par[a]

def union(a, b):
    global par
    ra = find(a)
    rb = find(b)
    if ra != rb:
        par[ra] = rb

n, m = map(int, input().split())

par = [i for i in range(n + 1)]

for _ in range (m):
    c, a, b = map(int, input().split())
    if (c == 0):
        union(a, b)
    else:
        print("YES" if find(a) == find(b) else "NO")