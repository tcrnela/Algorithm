n = int(input())
a = list(map(int, input().split()))
s = [0] * len(a)
s[-1] = a[-1]
ans = 0

for i in range (len(a)-2, 0, -1):
    s[i] = s[i+1] + a[i]
for i in range (len(a) - 1):
    ans += (a[i] * s[i+1]) % 1000000007
print(ans % 1000000007)