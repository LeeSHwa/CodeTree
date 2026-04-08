N = int(input())

grid =[list(input()) for _ in range(N)]

K = int(input())

'''
K 처리부터 시작
K // N을 통해 방향을 구하고,
K // N을 통해 포지션을 구하는데,
N, E 같은 경우는 그대로 그 값이 col, row 값이 됨
S, W 같은 경우는 N - 나머지 가 됨
'''

dr = [-1, 0, 1, 0] # N -> E -> S -> W
dc = [0, 1, 0, -1] 

first_dir = (K - 1) // N
rest = (K - 1) % N

if first_dir == 0:   # North
    pos = (0, rest)
    arrow = 2
elif first_dir == 1: # East
    pos = (rest, N - 1)
    arrow = 3
elif first_dir == 2: # South
    pos = (N - 1, N - 1 - rest)
    arrow = 0
else:                # West
    pos = (N - 1 - rest, 0)
    arrow = 1

row, col = pos

count = 0
'''
pos (0, 1), N 시작 
-> pos (0, 1) == \, N 닿았으니 E방향으로 튕김
-> 하지만 받아들이는 쪽에서는 W로 받아들임
-> 그래서 nr, nc는 이동은 E(0, 1) 만큼 가지만, arrow는 W임
'''
while True:
    count += 1

    if grid[row][col] == "/":
        if arrow == 0 or arrow == 2:
            arrow = (arrow + 1) % 4
        else:
            arrow = (arrow - 1) % 4
    else:
        if arrow == 0 or arrow == 2:
            arrow = (arrow - 1) % 4
        else:
            arrow = (arrow + 1) % 4

    nr = row + dr[arrow]
    nc = col + dc[arrow]

    if nr >= N or nr < 0 or nc >= N or nc < 0:
        break
    
    row = nr
    col = nc
    
    # if arrow == 0: arrow = 2
    # elif arrow == 1: arrow = 3
    # elif arrow == 2: arrow = 0
    # else: arrow = 1

print(count)