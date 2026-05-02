n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

ans = 101

for i in range(n):
    min_x = 101
    max_x = 0

    for j in range(n):
        if i == j:
            continue
        min_x = min(min_x, lines[j][0])
        max_x = max(max_x, lines[j][1])

    # print(min_x, max_x, ans, i)
    ans = min(ans, max_x - min_x)

print(ans)