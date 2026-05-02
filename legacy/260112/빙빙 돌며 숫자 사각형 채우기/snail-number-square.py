N, M = map(int, input().split()) # N * M grid

grid = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

row = 0
col = 0

dr = [0, 1,  0, -1]
dc = [1, 0, -1, 0]

# dirs = {"E" : 0, "S" : 1, "W" : 2, "N" : 3}

dir = 0

grid[0][0] = 1
visited[0][0] = True

last = grid[0][0]

while True:
    if last == N * M:
        break
    
    nr = row + dr[dir]
    nc = col + dc[dir]

    if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
        visited[nr][nc] = True
        grid[nr][nc] = last + 1
        

    else:
        dir = (dir + 1) % 4
        continue
    
    last = grid[nr][nc]
    row = nr
    col = nc

for i in range(N):
    print(" ".join(map(str, grid[i])))
