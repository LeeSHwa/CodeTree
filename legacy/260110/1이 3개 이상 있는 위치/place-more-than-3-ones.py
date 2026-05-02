N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

ans = 0

for row in range(N):
    for col in range(N):
        count = 0

        for dr, dc in dirs:
            nr, nc = row + dr, col + dc
            
            if 0 <= nr < N and 0 <= nc < N:
                if grid[nr][nc] == 1:
                    count += 1
        
        if count >= 3 :
            ans += 1

print(ans)
                