n = int(input())

checks = [tuple(map(int, input().split())) for _ in range(n)]

def cal_distance(current, next):
    return abs(checks[current][0] - checks[next][0]) + abs(checks[current][1] - checks[next][1])

min_distance = float('inf')

for passing in range(1, n - 1): # 건너 뛸 지점
    curr_distance = 0
    last_idx = 0

    for visiting in range(1, n):   # 방문할 지점
        if visiting == passing: # 만약 이 다음 방문할 지점이 건너 뛸 지점이라면
            continue                # 스킵
    
        curr_distance += cal_distance(last_idx, visiting) # 마지막 위치로부터 다음 위치까지의 거리를 더해줌
        last_idx = visiting

    min_distance = min(min_distance, curr_distance)

print(min_distance)
    
        