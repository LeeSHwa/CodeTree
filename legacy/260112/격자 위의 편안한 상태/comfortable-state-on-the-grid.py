N, M = map(int, input().split())
grid = [[False] * (N + 1) for _ in range(N + 1)]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(M):
    r, c = map(int, input().split())
    grid[r][c] = True

    count = 0
    ans = 0

    for dr, dc in dirs:
        nr = r + dr
        nc = c + dc

        if 0 < nr < N + 1 and 0 < nc < N + 1 and grid[nr][nc]:
            count += 1
        
    if count == 3:
        ans = 1

    print(ans)