n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n

max_value = 0

def backtrack(row, curr_min_value):
    global max_value
    
    if curr_min_value <= max_value:
        return
        
    if row == n:
        max_value = max(max_value, curr_min_value)
        return
    
    for col in range(n):
        if visited[col]:
            continue
        
        visited[col] = True
        
        backtrack(row + 1, min(curr_min_value, grid[row][col]))
        
        visited[col] = False

backtrack(0, float('inf'))

print(max_value)