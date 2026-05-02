n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
memo = [[-1] * n for _ in range(n)]

def init():
    memo[0][0] = grid[0][0]

    for col in range(1, n):
        memo[0][col] = max(memo[0][col - 1], grid[0][col])
    
    for row in range(1, n):
        memo[row][0] = max(memo[row - 1][0], grid[row][0])

init()

for row in range(1, n):
    for col in range(1, n):
        memo[row][col] = max(grid[row][col], min(memo[row - 1][col], memo[row][col - 1]))
    
print(memo[-1][-1])