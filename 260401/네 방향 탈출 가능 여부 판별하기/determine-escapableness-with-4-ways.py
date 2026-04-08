from collections import deque

q = deque()

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

q.append((0, 0))
visited[0][0] = True

while q:
    row, col = q.popleft()
    
    if visited[n-1][m-1]:
        print(1)
        exit()

    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and grid[nr][nc]:
            q.append((nr, nc))
            visited[nr][nc] = True

print(0)