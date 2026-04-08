N = int(input())

cube = {}

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            cube[(i, j)] = 1

print(sum(cube.values()))