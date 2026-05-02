n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(n)]
dp[0][-1] = grid[0][-1]

# dp[row][col] = max(dp[row-1][col] + grid[row][col], dp[row][col-1] + grid[row][col])

for row in range(n):
        
    for col in range(n - 1, -1, -1):
        if row == 0 and col == n-1:
            continue
        
        if row == 0:
            dp[row][col] = dp[row][col + 1] + grid[row][col]
            continue

        if col == n-1:
            dp[row][col] = dp[row-1][col] + grid[row][col]
            continue

        if row - 1 >= 0 and col + 1 < n:
            dp[row][col] = min(dp[row-1][col] + grid[row][col], dp[row][col+1] + grid[row][col])

print(dp[n-1][0])