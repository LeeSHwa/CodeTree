grid = [list(map(int, input().split())) for _ in range(19)]

dirs = [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0)] # NE, E, SE, S, SW, W, NW, N
dirs_dict = {}
stack = 0
pos = (0, 0)

for row in range(19):
    for col in range(19):

        if grid[row][col]:
            color = grid[row][col]
           
            for dr, dc in dirs:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < 19 and 0 <= nc < 19 and grid[nr][nc] == color:
                    stack = 2

                    while stack < 5:
                        nnr = nr + dr
                        nnc = nc + dc
                        
                        if grid[nnr][nnc] == color:
                            stack += 1
                            nr = nnr
                            nc = nnc

                        else: 
                            stack = 0
                            break

                    if stack == 5:
                        print(color)
                        print(nnr - dr * 2 + 1, nnc - dc * 2 + 1)
                        exit()

print(0)
                        