from collections import deque

n, k = map(int, input().split())

# grid = [list(map(int, input().split())) for _ in range(n)]
grid = []
walls = []

min_dist = float('inf')

for row in range(n):
    line = list(map(int, input().split()))

    for col in range(n):
        if line[col] == 1:
            walls.append((row, col))
    
    grid.append(line)

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
q = deque()
q.append((r1 - 1, c1 - 1))

def bfs():
    global min_dist
    que = q.copy()
    visited = [[False] * n for _ in range(n)]
    memory = {(r1 - 1, c1 - 1) : 0}
    visited[r1 - 1][c1 - 1] = True

    while que:
        row, col = que.popleft()

        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                memory[(nr, nc)] = memory[(row, col)] + 1
                
                if nr == r2 -1 and nc == c2 - 1:
                    min_dist = min(min_dist, memory[(nr, nc)])
                
                que.append((nr, nc))
                visited[nr][nc] = True



def backtrack(idx, cnt):
    
    if cnt == k:
        bfs()
        return
    
    if idx == len(walls):
        return
    
    r, c = walls[idx]
    grid[r][c] = 0

    backtrack(idx + 1, cnt + 1)

    grid[r][c] = 1
    
    backtrack(idx + 1, cnt)


backtrack(0, 0)

if min_dist == float('inf'):
    print(-1)
else:
    print(min_dist)