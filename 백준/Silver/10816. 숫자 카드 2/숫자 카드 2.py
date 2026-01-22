from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

d = defaultdict(int)
for i in range(n):
    d[a[i]] += 1
for i in range (m):
    print(d[b[i]], end=" ")