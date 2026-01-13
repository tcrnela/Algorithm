import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def union(a, b):
    global f
    aa = find(a)
    bb = find(b)

    if aa != bb:
        f[aa] = bb

def find(a):
    global f
    if (f[a] != a):
        f[a] = find(f[a])
    return f[a]

ans = 0
grp = []
v, e = map(int, input().split())
f = [i for i in range (v+1)]

for _ in range (e):
    a, b, c = map(int, input().split())
    grp.append((a, b, c))

grp.sort(key=lambda x: x[2])
for i in range (e):
    
    if (find(grp[i][0]) == find(grp[i][1])):
        continue
    union(grp[i][0], grp[i][1])
    ans += grp[i][2]
    
print(ans)