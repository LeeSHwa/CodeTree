from collections import deque

def solve():
    n, k = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]

    min_dist = float('inf')

    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())

    start_r, start_c = r1 - 1, c1- 1
    target_r, target_c = r2 -1, c2 - 1

    # 3차원 배열
    visited = [[[-1] * n for _ in range(n)] for _ in range(k + 1)]
    visited[0][start_r][start_c] = 0

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    q = deque()
    q.append((start_r, start_c, 0))
    
    while q:
        row, col, w = q.popleft()
        
        for dr, dc in dirs:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < n and 0 <= nc < n:
                if grid[nr][nc] == 0 and visited[w][nr][nc] == -1:
                    q.append((nr, nc, w))
                    visited[w][nr][nc] = visited[w][row][col] + 1

                    if nr == target_r and nc == target_c:
                        return visited[w][nr][nc]
                    
                elif grid[nr][nc] == 1 and w < k and visited[w + 1][nr][nc] == -1:
                    q.append((nr, nc, w + 1))
                    visited[w + 1][nr][nc] = visited[w][row][col] + 1

                    if nr == target_r and nc == target_c:
                        return visited[w + 1][nr][nc]
                    
                else: continue

    return -1

print(solve())