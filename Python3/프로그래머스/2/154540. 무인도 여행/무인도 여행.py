from collections import deque

def solution(maps):
    answer = []
    
    height = len(maps)
    width = len(maps[0])
    
    visited = [[False] * width for _ in range(height)]
    
    def bfs(row, col):
        q = deque()
        q.append((row, col))
        visited[row][col] = True
        foods = int(maps[row][col])
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < height and 0 <= nc < width and not visited[nr][nc] and maps[nr][nc] != 'X':
                    foods += int(maps[nr][nc])
                    visited[nr][nc] = True
                    q.append((nr, nc))
            
        return foods
    
    for i in range(height):
        for j in range(width):
            if not visited[i][j] and maps[i][j] != 'X':
                cnt = bfs(i, j)
                answer.append(cnt)
                
    return sorted(answer) if len(answer) != 0 else [-1]