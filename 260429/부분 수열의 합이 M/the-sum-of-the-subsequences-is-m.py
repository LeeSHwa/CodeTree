n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [[float('inf')] * (m + 1) for _ in range(n)]

for i in range(n):
    if nums[i] <= m:
        dp[i][nums[i]] = 1

    for j in range(1, m + 1):
        if j - nums[i] > 0:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j - nums[i]] + 1)
        else:
            dp[i][j] = min(dp[i][j], dp[i-1][j])

if dp[-1][-1] == float('inf'):
    print(-1)
else:
    print(dp[-1][-1])

# for line in dp:
#     print(*line)