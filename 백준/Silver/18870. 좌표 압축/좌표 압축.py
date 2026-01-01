from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))
b = list(set(a))
b.sort()

for i in range (n):
    print(bisect_left(b, a[i]), end=" ")