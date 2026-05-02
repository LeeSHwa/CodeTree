cube = [[0 for _ in range(2001)] for _ in range(2001)]

offset = 1000

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(offset + x1, offset + x2):
        cube[i][(offset + y1) : (offset + y2)] = [1] * (y2 - y1)

x1, y1, x2, y2 = map(int, input().split())

for i in range(offset + x1, offset + x2):
    cube[i][(offset + y1) : (offset + y2)] = [0] * (y2 - y1)

print(sum(sum(i) for i in cube))