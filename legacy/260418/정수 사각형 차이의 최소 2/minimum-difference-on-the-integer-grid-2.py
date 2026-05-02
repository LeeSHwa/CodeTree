n = int(input())
grid = []
nums = set()

for _ in range(n):
    line = list(map(int, input().split()))
    grid. append(line)
    
    for elem in line:
        nums.add(elem)

nums = sorted(list(nums))

start = grid[0][0]

# memo : 최소값이 L일때 가장 작은 최대값
memo = []

ans = float('inf')

def init(lower):
    global memo
    memo = [[float('inf')] * n for _ in range(n)]

    memo[0][0] = grid[0][0]

    for col in range(1, n):
        if grid[0][col] >= lower:
            memo[0][col] = max(memo[0][col - 1], grid[0][col])
        else:
            break

    for row in range(1, n):
        if grid[row][0] >= lower:
            memo[row][0] = max(memo[row - 1][0], grid[row][0])
        else:
            break

def dp(lower):

    for i in range(1, n):
        for j in range(1, n):
            if grid[i][j] >= lower:
                memo[i][j] = max(grid[i][j], min(memo[i-1][j], memo[i][j-1]))

for lower in nums:
    if lower > start:
        break
    init(lower)
    

    dp(lower)

    if memo[n-1][n-1] != float('inf'):
        ans = min(ans, memo[n-1][n-1] - lower)

print(ans)