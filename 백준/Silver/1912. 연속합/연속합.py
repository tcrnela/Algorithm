n = int(input())
a = list(map(int, input().split()))
dp = []
for i in range (n):
    dp.append(a[i])

for i in range (1, n):
    if dp[i] + dp[i-1] > dp[i]:
        dp[i] = dp[i] + dp[i-1]

print(max(dp))