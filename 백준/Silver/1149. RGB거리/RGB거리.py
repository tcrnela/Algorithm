n = int(input())
rgb = []
dp = [[float("inf")] * 3 for _ in range (n)]

for _ in range (n):
    q, w, e = map(int, input().split())
    rgb.append((q, w, e))

dp[0][0] = rgb[0][0]
dp[0][1] = rgb[0][1]
dp[0][2] = rgb[0][2]

for i in range (1, n):
    for j in range (3):
        for k in range (3):
            if j == k: continue
            if dp[i][j] > dp[i-1][k] + rgb[i][j]:
                dp[i][j] = dp[i-1][k] + rgb[i][j]
print(min(dp[n-1]))