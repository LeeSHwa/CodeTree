x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

width = max(a2, x2) - min(a1, x1)
height = max(y2, b2) - min(y1, b1)

print(width * height)