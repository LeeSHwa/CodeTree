N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]

dirs = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)] # NE, E, SE, S, SW, W, NW, N

count = 0

for row in range(N):
    for col in range(M):

        if grid[row][col] == 'L':
           
            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] == 'E':

                    nnr = nr + dr
                    nnc = nc + dc
                        
                    if 0 <= nnr < N and 0 <= nnc < M and grid[nnr][nnc] == 'E':
                        count += 1

print(count)