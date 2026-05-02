n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort(key = lambda x : (x[0], x[1]))

x = [p[0] for p in points]
y = [p[1] for p in points]

max_extent = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if (x[i] == x[j] or x[j] == x[k] or x[k] == x[i]) and (y[i] == y[j] or y[j] == y[k] or y[k] == y[i]):
                width = max(x[i], x[j], x[k]) - min(x[i], x[j], x[k])
                height = max(y[i], y[j], y[k]) - min(y[i], y[j], y[k])

                extent = width * height
                max_extent = max(max_extent, extent)


print(max_extent)
            