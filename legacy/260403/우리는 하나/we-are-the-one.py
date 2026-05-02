from collections import deque

n, k, u, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

to_explore = [(x, y) for x in range(n) for y in range(n)]

def can_go(row, col, val):
    if row < 0 or row >= n or col < 0 or col >= n:
        return False

    return u <= abs(grid[row][col] - val) <= d


def bfs(starts):
    q = deque()
    q.extend(starts)
    cnt = len(q)
    visited = [[False] * n for _ in range(n)]

    for r, c in q:
        visited[r][c] = True
    
    while q:
        row, col = q.popleft()

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = row + dr
            nc = col + dc

            if can_go(nr, nc, grid[row][col]) and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = True 
                cnt += 1

    return cnt

starts = []

ans = 0

def backtrack(idx):
    global ans

    if len(starts) == k:
        bfs(starts)
        curr = bfs(starts)
        ans = max(ans, curr)
        return

    if idx == n*n:
        return

    starts.append(to_explore[idx])
    
    backtrack(idx + 1)

    starts.pop()
    
    backtrack(idx + 1)

backtrack(0)

print(ans)