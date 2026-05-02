n, m = map(int, input().split())

pos = [tuple(map(int, input().split())) for _ in range(n)]

select_array = []

ans = float('inf')

def calc():
    max_distance = 0
    for i in range(m - 1):
        for j in range(i + 1, m):
            max_distance = max(max_distance, (select_array[i][0] - select_array[j][0]) ** 2 + (select_array[i][1] - select_array[j][1]) ** 2)
    
    return max_distance


def backtrack(idx, select_cnt):
    global ans

    # 종료조건
    if select_cnt == m:
        current_max = calc()
        ans = min(ans, current_max)
        return
    
    # 가지치기
    if n - idx < m - select_cnt:
        return

    # 탐색 끝
    if idx == n:
        return
    
    select_array.append(pos[idx])
    backtrack(idx + 1, select_cnt + 1)
    select_array.pop()

    backtrack(idx + 1, select_cnt)

backtrack(0, 0)
print(ans)