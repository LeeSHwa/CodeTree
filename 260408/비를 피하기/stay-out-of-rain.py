from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

escape = [[0] * n for _ in range(n)]


def bfs(row, col):
    q = deque()
    q.append((row, col))
    visited = [[False] * n for _ in range(n)]
    visited[row][col] = True
    dist = {}
    dist = {(row, col) : 0}

    while q:
        r, c = q.popleft()

        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and not grid[nr][nc] == 1:            
                dist[(nr, nc)] = dist[(r, c)] + 1

                if grid[nr][nc] == 3:
                    escape[row][col] = dist[(nr, nc)]
                    return

                visited[nr][nc] = True
                q.append((nr, nc))                

    escape[row][col] = -1

for row in range(n):
    for col in range(n):
        if grid[row][col] == 2:
            bfs(row, col)

for line in escape:
    print(*line)