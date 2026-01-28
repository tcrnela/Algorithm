n = int(input())
a = [0] * (n+2)
dp = [0] * (n+2)

for i in range (1, n+1):
    a[i] = int(input())

dp[1] = a[1]
dp[2] = a[2] + a[1]

for i in range (3, n+1):
    for j in range (3, i+1):
        dp[i] = max(dp[i], dp[i-j+1] + a[i], dp[i-j] + a[i-1] + a[i])

print(max(dp))