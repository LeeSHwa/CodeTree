n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

visited = [[False] * n for _ in range(n)]

boom_cnt = 0
max_depth = -1
flag = False

def dfs(row, col):
    global depth
    
    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc
        
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[row][col] == grid[nr][nc]:
            visited[nr][nc] = True
            depth += 1
            dfs(nr, nc)


for row in range(n):
    for col in range(n):
        if not visited[row][col]:
            depth = 1
            visited[row][col] = True
            flag = False
            dfs(row, col)

            if depth >= 4:
                boom_cnt += 1
            max_depth = max(max_depth, depth)

print(boom_cnt, max_depth)