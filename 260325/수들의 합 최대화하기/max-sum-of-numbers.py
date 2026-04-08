n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited_col = [False] * n

ans = 0

def backtrack(row, current_sum):
    global ans

    if row == n:
        ans = max(ans, current_sum)
        return
    
    for col in range(n):
        if visited_col[col]:
            continue
        
        visited_col[col] = True
        
        backtrack(row + 1, current_sum + grid[row][col])

        visited_col[col] = False

backtrack(0, 0)
print(ans)