import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0
for i in range (6):
    t = a[i] // b
    cnt += t
    a[i] -= t * b
    if (a[i] > 0):
        cnt += 1

print(cnt)
print(n//c, end=" ")
print(n%c)