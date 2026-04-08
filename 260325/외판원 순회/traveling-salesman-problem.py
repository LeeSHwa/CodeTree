n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
min_price = float('inf')

def backtrack(start, explored_cnt, curr_price):
    global min_price

    if explored_cnt == n - 1 and grid[start][0] != 0:
        total_price = curr_price + grid[start][0]
        min_price = min(min_price, total_price)

        return
    
    if curr_price >= min_price:
        return
    
    for end in range(1, n):
        if end == start or visited[end] or grid[start][end] == 0:
            continue
        visited[end] = True
        
        backtrack(end, explored_cnt + 1, curr_price + grid[start][end])

        visited[end] = False

backtrack(0, 0, 0)

print(min_price)