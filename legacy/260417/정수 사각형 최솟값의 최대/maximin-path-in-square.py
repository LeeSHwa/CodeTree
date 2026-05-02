n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * n for _ in range(n)]

def init():
    dp[0][0] = grid[0][0]
    
    # 첫 번째 행 채우기
    for col in range(1, n):
        dp[0][col] = min(dp[0][col - 1], grid[0][col])
    
    # 첫 번째 열 채우기
    for row in range(1, n):
        dp[row][0] = min(dp[row - 1][0], grid[row][0])


init()

# 나머지 칸 채우기
for row in range(1, n):
    for col in range(1, n):
        dp[row][col] = max(min(dp[row-1][col], grid[row][col]), min(dp[row][col-1], grid[row][col]))

print(dp[n-1][n-1])