N = int(input())

dots = [tuple(map(int, input().split())) for _ in range(N)]

ans = float('inf')

for i in range(N):
    new_dots = dots[i+1:] + dots[:i]
    
    x1, y1 = float('inf'), float('inf') # 좌 하단
    x2, y2 = -1, -1                     # 우 상단
    
    for x, y in new_dots:
        x1, y1 = min(x1, x), min(y1, y)
        x2, y2 = max(x2, x), max(y2, y)
        
    square = (y2 - y1) * (x2 - x1)
    ans = min(ans, square)    

print(ans)