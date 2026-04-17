n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# memo : 해당 위치에서 뻗어나갈 수 있는 노드의 수
memo = [[-1] * n for _ in range(n)]


def dfs(row, col):
    if memo[row][col] != -1:
        return memo[row][col]

    memo[row][col] = 1
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > grid[row][col]:
            memo[row][col] = max(memo[row][col], dfs(nr, nc) + 1)

    return memo[row][col]


ans = 0
for row in range(n):
    for col in range(n):
        ans = max(ans, dfs(row, col))

print(ans)