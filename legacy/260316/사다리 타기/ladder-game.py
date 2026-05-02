n, m = map(int, input().split())

ladders = [tuple(map(int, input().split())) for _ in range(m)]

MAX_HEIGHT = 16

grid = [[0] * n for _ in range(MAX_HEIGHT)]


def apply_grid(row, col, val):
    if val == 1:
        grid[row - 1][col - 1] = 1
    else:
        grid[row - 1][col - 1] = 0

def play_game():
    pos = list(range(1, n + 1))

    for depth in range(MAX_HEIGHT):
        line = grid[depth]

        for idx in range(n - 1):
            if line[idx]:
                pos[idx], pos[idx + 1] = pos[idx + 1], pos[idx]
    
    return pos

# 1. 정답 배열을 구하기 위해 apply 호출
for i in range(m):
    col, row = ladders[i]
    apply_grid(row, col, 1)

# 2. 정답배열 저장
ans_pos = play_game()

# 3. 원상복구
for i in range(m):
    col, row = ladders[i]
    apply_grid(row, col, -1)

min_cnt = n

# 재귀
def recurr(elem_idx, curr_cnt):
    global min_cnt
    
    # 0. 가지치기
    if curr_cnt >= min_cnt:
        return
    
    # 1. 종료조건
    if elem_idx == m:
        curr_pos = play_game()
        
        if curr_pos == ans_pos:
            min_cnt = curr_cnt
        
        return

    c, r = ladders[elem_idx]

    # 2. 적용
    apply_grid(r, c, 1)

    # 3. 적용 후탐색
    recurr(elem_idx + 1, curr_cnt + 1)

    # 4. 해제
    apply_grid(r, c, -1)

    # 5. 적용하지 않고 탐색
    recurr(elem_idx + 1, curr_cnt)

recurr(0, 0)

print(min_cnt)