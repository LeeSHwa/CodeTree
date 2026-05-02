N = int(input())

grid = [[0] * N for _ in range(N)]

row = N // 2
col = N // 2

dr = [0, 1,  0, -1]
dc = [1, 0, -1, 0]

# dirs = {"E" : 0, "S" : 1, "W" : 2, "N" : 3}

dir = 0

grid[N // 2][N // 2] = 1

last = 1

array = []

for i in range(1, N):
    array.append(i)
    array.append(i)
    if i == N - 1:
        array.append(i)

for count in array:
    for i in range(count):
        nr = row + dr[dir]
        nc = col + dc[dir]
        
        grid[nr][nc] = last + 1
        
        last = grid[nr][nc]

        row = nr
        col = nc
    dir = (dir - 1) % 4
            


for i in range(N):
    print(" ".join(map(str, grid[i])))
