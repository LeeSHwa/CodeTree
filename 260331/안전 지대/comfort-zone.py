import sys

sys.setrecursionlimit(10**6) 

n, m = map(int, input().split())

grid = []
max_value = 0

for _ in range(n):
    line = list(map(int, input().split()))
    max_value = max(max_value, max(line))
    grid.append(line)

visited = [[False] * m for _ in range(n)]

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def refresh_visited():
    global visited
    visited = [[False] * m for _ in range(n)]

def is_inrange(row, col):
    return 0 <= row < n and 0 <= col < m

def is_possible(row, col, k):
    if not is_inrange(row, col):
        return False

    if grid[row][col] - k < 1:
        return False
    
    if visited[row][col]:
        return False
    
    return True

def dfs(row, col, k):
    
    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc

        if is_possible(nr, nc, k):
            visited[nr][nc] = True
            dfs(nr, nc, k)

max_cnt = -1
min_k = float('inf')

for k in range(1, max_value + 1):

    refresh_visited()

    curr_cnt = 0

    for row in range(n):
        for col in range(m):
            if is_possible(row, col, k):
                curr_cnt += 1
                visited[row][col] = True
                dfs(row, col, k)
        
    if curr_cnt > max_cnt:
        max_cnt = curr_cnt
        min_k = k

print(min_k, max_cnt)
                