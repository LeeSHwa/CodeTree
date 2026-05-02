n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]

dp[0][0] = 1
max_cnt = 1

for row in range(1, n):
    for col in range(1, m):
        
        for i in range(row):
            for j in range(col):
                if dp[i][j] != -1 and grid[row][col] > grid[i][j]:
                    dp[row][col] = max(dp[row][col], dp[i][j] + 1)
                    if dp[row][col] > max_cnt:
                        max_cnt = dp[row][col]

print(max_cnt)