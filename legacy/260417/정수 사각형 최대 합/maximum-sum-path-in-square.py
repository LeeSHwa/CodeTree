n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(n)]
dp[0][0] = grid[0][0]

# dp[row][col] = max(dp[row-1][col] + grid[row][col], dp[row][col-1] + grid[row][col])

for row in range(n):
        
    for col in range(n):
        if row == 0 and col == 0:
            continue
        
        if row == 0:
            dp[row][col] = dp[row][col - 1] + grid[row][col]
            continue

        if col == 0:
            dp[row][col] = dp[row-1][col] + grid[row][col]
            continue

        if row - 1 >= 0 and col - 1 >= 0:
            dp[row][col] = max(dp[row-1][col] + grid[row][col], dp[row][col-1] + grid[row][col])

print(dp[n-1][n-1])