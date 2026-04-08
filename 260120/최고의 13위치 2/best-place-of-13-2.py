N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

max_value = -1 

for bar1_row in range(N):
    for bar1_col in range(N-2):
        bar1 = grid[bar1_row][bar1_col] + grid[bar1_row][bar1_col + 1] + grid[bar1_row][bar1_col + 2]
        
        if (bar1_col + 2) + 3 < N:
            bar2_row = bar1_row
            for bar2_col in range(bar1_col + 3, N - 2):
                bar2 = grid[bar2_row][bar2_col] + grid[bar2_row][bar2_col + 1] + grid[bar2_row][bar2_col + 2]

                max_value = max(max_value, bar1 + bar2)

        for bar2_row in range(bar1_row + 1, N):
            for bar2_col in range(N-2):
                bar2 = grid[bar2_row][bar2_col] + grid[bar2_row][bar2_col + 1] + grid[bar2_row][bar2_col + 2]
                max_value = max(max_value, bar1 + bar2)


print(max_value)