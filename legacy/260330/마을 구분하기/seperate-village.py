n = int(input())

towns = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

cnt = 0

def dfs(row, col):
    global cnt

    for dr, dc in dirs:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and towns[nr][nc]:
            visited[nr][nc] = True
            cnt += 1
            dfs(nr, nc)
    


town = []

for row in range(n):
    for col in range(n):
        if towns[row][col] and not visited[row][col]:
            visited[row][col] = True
            cnt = 1
            dfs(row, col)
            town.append(cnt)

town.sort()

print(len(town))
for i in town:
    print(i)