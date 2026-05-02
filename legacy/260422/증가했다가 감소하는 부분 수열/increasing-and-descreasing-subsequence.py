n = int(input())

nums = list(map(int, input().split()))


dp = [[1] * n for _ in range(2)]

ans = -1

for i in range(1, n):
    
    for j in range(i):

        if nums[i] > nums[j]:
            dp[0][i] = max(dp[0][i], dp[0][j] + 1)

        elif nums[i] < nums[j]:
            dp[1][i] = max(dp[1][i], dp[1][j] + 1, dp[0][j] + 1)

    ans = max(ans, dp[0][i], dp[1][i])

print(ans)