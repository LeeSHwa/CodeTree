from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())

r -= 1
c -= 1

flag = True

def bfs(row, col, val):
    global flag

    array = [0]
    q = deque()
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    visited = [[False] * n for _ in range(n)]

    q.append((row, col))
    visited[row][col] = True

    while q:
        r1, c1 = q.popleft()

        for dr, dc in dirs:
            nr = r1 + dr
            nc = c1 + dc

            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] < val and not visited[nr][nc]:
                flag = False

                if  grid[nr][nc] > array[0]:
                    array = [grid[nr][nc], (nr, nc)]
                elif grid[nr][nc] == array[0]:
                    array.append((nr, nc))
                
                visited[nr][nc] = True
                q.append((nr, nc))


    if len(array) > 1:
        sorted_array = sorted(array[1:], key= lambda x : (x[0], x[1]))
        return sorted_array[0] 

    else:
        return array[0]
        

for _ in range(k):
    flag = True
    temp = bfs(r, c, grid[r][c])
    
    if flag:
        print(r + 1, c + 1)
        exit()
    
    r, c = temp

print(r + 1, c + 1)