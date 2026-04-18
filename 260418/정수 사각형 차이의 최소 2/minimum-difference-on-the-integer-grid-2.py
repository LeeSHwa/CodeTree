n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# memo : 해당 위치에서 뻗어나갈 수 있는 노드의 수
memo = [[-1] * n for _ in range(n)]

def init():
    memo[0][0] = [grid[0][0], grid[0][0]]

    # for row in range(1, n):
    #     memo[row][0] = [max(memo[row - 1][0][0], grid[row][0]), min(memo[row - 1][0][1], grid[row][0])]
    
    # for col in range(1, n):
    #     memo[0][col] = [max(memo[0][col - 1][0], grid[0][col]), min(memo[0][col - 1][1], grid[0][col])]

init()

ans = float('inf')

def backtrack(row, col):
    global ans

    if row == n - 1 and col == n - 1:
        diff = memo[-1][-1][0] - memo[-1][-1][1]
        ans = min(ans, diff)    
    
    for dr, dc in [(1, 0), (0, 1)]:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < n and 0 <= nc < n:
            temp = memo[nr][nc]

            memo[nr][nc] = [max(memo[row][col][0], grid[nr][nc]), min(memo[row][col][1], grid[nr][nc])]
            backtrack(nr, nc)
            
            memo[nr][nc] = temp

backtrack(0, 0)

print(ans)
