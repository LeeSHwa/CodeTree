# 1. 시작시 테두리는 항상 0임 
# 그렇기 때문에 겉만 핥으면서 이게 air인지, glacier인지 기록하는 두 개의 queue가 필요
# air를 기준으로 bfs를 돌고
# 탐색을 끝마쳤다면 겉부분에 있는 glacier 큐만 남았을거임
# 탐색 밖에서 glacier의 길이를 재고, last로 저장해 둔 다음, 실제 grid의 값을 변경
# 그리고 air = glacier를 통해, 시작점을 정해줌

from collections import deque

gla_q = deque()

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

def bfs(air_q):
    gla_q = deque()

    while air_q:
        row, col = air_q.popleft()

        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nr = row + dr
            nc = col + dc
            
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if grid[nr][nc]:
                    gla_q.append((nr, nc))
                else:
                    air_q.append((nr, nc))
                
                visited[nr][nc] = True
    
    return gla_q

last = -1 
cnt = 0
air_q = deque()
air_q.append((0, 0))

while last != 0:

    gla_q = bfs(air_q)
    
    if len(gla_q) == 0:
        print(cnt, last)
        break
    
    cnt += 1
    last = len(gla_q)

    air_q = gla_q