n, m = map(int, input().split())
nums = list(map(int, input().split()))

dp = [[float('inf')] * (m + 1) for _ in range(n)]

# base
dp[0][nums[0]] = 1

for i in range(1, n):
    if nums[i] <= m:
        dp[i][nums[i]] = nums[i]

    for j in range(1, m + 1):
        
        dp[i][j] = min(dp[i-1][j], dp[i-1][j - nums[i]] + 1)


if dp[-1][-1] == float('inf'):
    print(-1)
else:
    print(dp[-1][-1])