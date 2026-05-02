n = int(input())
jumps = list(map(int, input().split()))

min_cnt = 10

def backtrack(idx, curr_cnt):
    global min_cnt
    if curr_cnt >= min_cnt:
        return  

    if idx == n - 1:
        min_cnt = min(min_cnt, curr_cnt)
        return

    possible_jump = jumps[idx]

    if possible_jump == 0:
        return
    
    for i in range(1, possible_jump + 1):
        backtrack(idx + i, curr_cnt + 1)

backtrack(0, 0)

if min_cnt == 10:
    print(-1)
else:
    print(min_cnt)