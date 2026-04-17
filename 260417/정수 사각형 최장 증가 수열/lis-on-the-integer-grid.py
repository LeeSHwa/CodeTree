from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# memo : 해당 위치에서 뻗어나갈 수 있는 노드의 수
memo = [[-1] * n for _ in range(n)]

def bfs(row, col):
    visited = [[False] * n for _ in range(n)]

    q = deque()

    # row, col, 이동 횟수
    q.append((row, col, 1))
    visited[row][col] = True

    max_value = 0

    while q:
        r, c, cnt = q.popleft()
        max_value = max(cnt, max_value)

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc


            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > grid[r][c]:
                # 만약 탐색하려는 memo[nr][nc]의 값이 이미 계산되어 있다면
                if memo[nr][nc] != -1 :
                    # 그 값을 가져와서 바로 적용
                    memo[row][col] = memo[nr][nc] + cnt
                    continue
                
                # 처음 가보는 길이라면
                if not visited[nr][nc] :
                    visited[nr][nc] = True
                    q.append((nr, nc, cnt + 1))
    
    memo[row][col] = max(memo[row][col], max_value)
        

ans = 0
for row in range(n):
    for col in range(n):
        bfs(row, col)
        ans = max(ans, memo[row][col])

print(ans)