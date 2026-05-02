n = int(input())
position = {}
exist = []

for row in range(n):
    line = list(input())

    for col in range(n):
        if line[col] == 'S':
            position['start'] = (row, col)
        elif line[col] == 'E':
            position['end'] = (row, col)
        elif line[col] != '.':
            position[int(line[col])] = (row, col)
            exist.append(int(line[col]))

exist.sort()

visited = []
ans = float('inf')

def cal_dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def backtrack(pos, idx, move_count):
    global ans
    
    row, col = pos

    # 가지치기
    if move_count >= ans:
        return
    # 종료조건
    if len(visited) == 3:
        ans = min(ans, move_count + cal_dist(position['end'], pos))
        return
    
    # 탐색이 모두 끝났을 때
    if idx == len(exist):
        return

    # 1. 골랐을 때
    visited.append(exist[idx])
    backtrack(position[exist[idx]], idx + 1, move_count + cal_dist(position[exist[idx]], pos))
    visited.pop()

    # 2. 고르지 않았을 때
    backtrack(pos, idx + 1, move_count)

backtrack(position['start'], 0, 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)