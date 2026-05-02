N, T = map(int, input().split())
command = list(input())

grid = [list(map(int, input().split())) for _ in range(N)]

row, col = N // 2, N // 2

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1] 
#     N, E, S, W

dir = 0
total = grid[row][col]

for comm in command:
    if comm == "L":
        dir = (dir - 1) % 4
    elif comm == "R":
        dir = (dir + 1) % 4
    else:
        nr = row + dr[dir]
        nc = col + dc[dir]

        if 0 <= nr < N and 0 <= nc < N:
            row = nr
            col = nc
            
            total += grid[row][col]

print(total)
