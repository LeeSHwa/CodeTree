n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

# [최대값 , 최소값]로 저장 예정
memo = [[None] * n for _ in range(n)]

def init():
    memo[0][0] = [grid[0][0], grid[0][0]]

    for row in range(1, n):
        memo[row][0] = [max(memo[row - 1][0][0], grid[row][0]), min(memo[row - 1][0][1], grid[row][0])]
    
    for col in range(1, n):
        memo[0][col] = [max(memo[0][col - 1][0], grid[0][col]), min(memo[0][col - 1][1], grid[0][col])]

init()

def cal(row, col):
    max_1, min_1 = memo[row - 1][col]
    max_2, min_2 = memo[row][col - 1]
    val = grid[row][col]


    if max_1 - min_1 > max_2 - min_2: # 1. 2번째가 차이가 더 적다면
        return [max(max_2, val), min(min_2, val)]
    else:
        return [max(max_1, val), min(min_1, val)]


for row in range(1, n):
    for col in range(1, n):
        memo[row][col] = cal(row, col)

        
# for line in memo:
#     print(*line)

print(memo[n-1][n-1][0] - memo[n-1][n-1][1])