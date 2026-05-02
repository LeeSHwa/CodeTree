from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dist_grid = [[0] * m for _ in range(n)]

def bfs(row, col):
    q = deque()
    q.append((row, col))

    visited = [[False] * m for _ in range(n)]
    visited[row][col] = True
    
    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] and not visited[nr][nc]:
                dist_grid[nr][nc] = dist_grid[r][c] + 1
                visited[nr][nc] = True
                
                q.append((nr, nc))

bfs(0, 0)

ans = dist_grid[n-1][m-1]

if ans == 0:
    print(-1)
else:
    print(ans)
