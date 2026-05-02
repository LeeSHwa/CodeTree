n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dirs = [(1, 0), (0, 1)]

def dfs(row, col):

    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and edges[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc)

dfs(0, 0)

if visited[n - 1][m - 1] == True:
    print(1)
else:
    print(0)
    
    
