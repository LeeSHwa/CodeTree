N = int(input())
MAX_RANGE = 201
OFFSET = 100

grid = [[0 for _ in range(MAX_RANGE)] for _ in range(MAX_RANGE)]

for color in range(N):
    x1, y1, x2, y2 = map(int, input().split())
        
    x1, x2 = x1 + OFFSET, x2 + OFFSET
    y1, y2 = y1 + OFFSET, y2 + OFFSET
    
    BLUE = ["B"] * (x2 - x1)
    RED = ["R"] * (x2 - x1)
    
    for i in range(y2-y1):
        if color % 2 == 0:
            grid[y1 + i][x1:x2] = RED
        else:
            grid[y1 + i][x1:x2] = BLUE


area = 0
for i in range(MAX_RANGE):
    for j in range(MAX_RANGE):
        if grid[i][j] == "B":
            area += 1

print(area)
        