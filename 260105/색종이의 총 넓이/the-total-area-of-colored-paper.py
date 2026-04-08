# n = int(input())
# points = [tuple(map(int, input().split())) for _ in range(n)]
# x, y = zip(*points)
# x, y = list(x), list(y)

# Please write your code here.

MAX_RANGE = 201
OFFSET = 100

cube = [[0 for _ in range(MAX_RANGE)] for _ in range(MAX_RANGE )]

n = int(input())

for _ in range(n):
    row, col = map(int, input().split())
    row += OFFSET
    col += OFFSET

    for i in range(8):
        cube[row + i][col : col + 8] = [1] * 8
        
        
print(sum(sum(i) for i in cube))