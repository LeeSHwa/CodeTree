n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dirr_grid = [list(map(int, input().split())) for _ in range(n)]

dirrection = {1 : (-1, 0), 2 : (-1, 1), 3 : (0, 1), 4 : (1, 1),
              5 : (1, 0), 6 : (1, -1), 7 : (0, -1), 8 : (-1, -1)}


row, col = map(int, input().split())

row -= 1
col -= 1

def found(r, c, dir):
    array = []
    dr, dc = dir

    while True:
        nr = r + dr
        nc = c + dc

        if 0 <= nr < n and 0 <= nc < n:
            array.append((nr, nc))
            r, c = nr, nc
        else:
            break

    return array

max_cnt = 0
def backtrack(r, c, dirr, cnt):
    global max_cnt

    max_cnt = max(max_cnt, cnt)

    search_array = found(r, c, dirrection[dirr_grid[r][c]])
        
    for nr, nc in search_array:
        if grid[nr][nc] > grid[r][c]:
            backtrack(nr, nc, dirrection[dirr_grid[nr][nc]], cnt + 1)


backtrack(row, col, dirrection[dirr_grid[row][col]], 0)
print(max_cnt)
