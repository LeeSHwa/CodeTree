from collections import deque
n, k, m = map(int, input().split())

grid = []
rocks = []

for row in range(n):
    line = list(map(int, input().split()))

    for col in range(n):
        if line[col]:
            rocks.append((row, col))

    grid.append(line)

starts = deque()

for _ in range(k):
    r, c = map(int, input().split())
    starts.append((r-1, c-1))


def bfs():
    q = starts.copy()
    visited = [[False] * n for _ in range(n)]
    
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    cnt = 0

    while q:
        row, col = q.popleft()

        for dr, dc in dirs:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and not visited[nr][nc]:
                q.append((nr, nc))
                cnt += 1
                visited[nr][nc] = True
    

    return cnt
    

ans = 0

def backtrack(idx, depth):
    global ans

    if depth == m:
        cnt = bfs()
        ans = max(ans, cnt)
        return

    if idx == len(rocks):
        return

    r, c = rocks[idx]
    grid[r][c] = 0

    backtrack(idx + 1, depth + 1)

    grid[r][c] = 1

    backtrack(idx + 1, depth)
    
backtrack(0, 0)

print(ans)