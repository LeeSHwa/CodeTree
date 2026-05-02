x1, x2, x3, x4 = map(int, input().split())

if x1 > x4 or x3 > x2:
    print("nonintersecting")
else:
    print("intersecting")