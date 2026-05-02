from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

starts = [tuple(map(int, input().split())) for _ in range(k)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

visited = [[False] * n for _ in range(n)]

array = []

def can_go(row, col):
    if row >= n or row < 0 or col >= n or col < 0:
        return False
    
    if visited[row][col]:
        return False
    
    if grid[row][col]:
        return False
    
    return True


def bfs(r, c):
    
    temp = []
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    temp.append((r, c))
    
    while q:
        row, col = q.popleft()
        
        for dr, dc in dirs:
            nr = row + dr
            nc = col + dc

            if can_go(nr, nc):
                visited[nr][nc] = True
                q.append((nr, nc))
                temp.append((nr, nc))


    return temp
order = 1
for r in range(n):
    for c in range(n):
        if grid[r][c] == 0 and not visited[r][c]:
            array = bfs(r, c)
            cnt = len(array)

            for row, col in array:
                grid[row][col] = [order, cnt]
            
            order += 1

checked_order = [False] * (order + 1)

ans = 0
for row, col in starts:
    o, v = grid[row - 1][col - 1]
    
    if checked_order[o]:
        continue
    else:
        ans += v
        checked_order[o] = True

print(ans)
