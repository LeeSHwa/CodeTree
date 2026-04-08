N, M = map(int, input().split()) # N * M grid

grid = [[0] * M for _ in range(N)]

row = 0
col = 0

dr = [0, 1,  0, -1]
dc = [1, 0, -1, 0]

# dirs = {"E" : 0, "S" : 1, "W" : 2, "N" : 3}

dir = 0

grid[0][0] = 65 # 65 : A ~ 88 : X

last = grid[0][0]

count = 0
while True:
    if count == N * M - 1:
        break

    nr = row + dr[dir]
    nc = col + dc[dir]

    if 0 <= nr < N and 0 <= nc < M and not grid[nr][nc]:
        if grid[row][col] == 90:
            grid[nr][nc] = 65
        else:
            grid[nr][nc] = last + 1
        
    else:
        dir = (dir + 1) % 4
        continue
    
    last = grid[nr][nc]
    row = nr
    col = nc
    count += 1

for i in range(N):
    for j in range(M):
        print(chr(grid[i][j]), end = " ")
    print()

