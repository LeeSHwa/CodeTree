from collections import deque

def solve():
    n, k = map(int, input().split())

    rotten_mandarin = [[0] * n for _ in range(n)]
    starts = deque()

    for row in range(n):
        line = list(map(int, input().split()))

        for col in range(n):
            if line[col] == 0:
                rotten_mandarin[row][col] = -1
            elif line[col] == 2:
                starts.append((row, col, 0))
            else:
                rotten_mandarin[row][col] = -2

    while starts:
        row, col, cnt = starts.popleft()

        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = row + dr
            nc = col + dc

            if 0 <= nr < n and 0 <= nc < n and rotten_mandarin[nr][nc] == -2:
                starts.append((nr, nc, cnt + 1))
                rotten_mandarin[nr][nc] = cnt + 1

    return rotten_mandarin

ans = solve()

for line in ans:
    print(*line)