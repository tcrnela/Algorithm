n = int(input())
a = []
ans = []
for i in range (n):
    t = int(input())
    a.append(t)
a.sort()
for i in range (n):
    ans.append(a[i] * (n-i))
print(max(ans))