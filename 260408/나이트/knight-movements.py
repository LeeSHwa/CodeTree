from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
dirs = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)]

grid = [[0] * n for _ in range(n)]

visited = [[False] * n for _ in range(n)]

q = deque()
q.append((r1, c1))

def bfs():
    
    while q:
        row, col = q.popleft()
        
        visited[row][col] = True

        for dr, dc in dirs:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                grid[nr][nc] = grid[row][col] + 1
                visited[nr][nc] = True
                q.append((nr, nc))
            
        if grid[r2][c2]:
            return grid[r2][c2]
    
    if not visited[r2][c2]:
        return -1
    else:
        return 0


print(bfs())