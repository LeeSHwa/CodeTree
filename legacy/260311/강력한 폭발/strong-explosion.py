n = int(input())
booms = []
grid = [[0] * n for _ in range(n)]
ans = 0

for row in range(n):
    line = list(map(int, input().split()))

    for col in range(n):
        if line[col]:
            booms.append((row, col))
            grid[row][col] = 1

depth = len(booms) # 폭탄 개수만큼 들어감

types = { # 터지는 타입
    'first' : [(-2, 0), (-1, 0), (1, 0), (2, 0)],
    'second' : [(1, 0), (-1, 0), (0, 1), (0, -1)],
    'third' : [(1, 1), (1, -1), (-1, -1), (-1, 1)]
}



def count_boom():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 1:
                cnt += 1
    
    return cnt

def apply_boom(row, col, b_type, val):
   
    for dr, dc in types[b_type]:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < n and 0 <= nc < n:
            grid[nr][nc] += val
    
def recurr(array, dep):
    global ans

    if dep == depth:
        curr = count_boom()
        ans = max(ans, curr)
        return

    r, c = array[dep]

    for type in types:
        apply_boom(r, c, type, 1)
        recurr(array, dep + 1)
        apply_boom(r, c, type, -1)
        
recurr(booms, 0)
print(ans)