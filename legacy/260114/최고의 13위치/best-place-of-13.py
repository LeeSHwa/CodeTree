N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

max_value = -1

for row in range(N):
    for col in range(N-2):
        max_value = max(max_value, grid[row][col] + grid[row][col + 1] + grid[row][col + 2])

print(max_value)