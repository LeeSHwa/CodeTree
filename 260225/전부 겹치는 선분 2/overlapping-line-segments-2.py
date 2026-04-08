n = int(input())

lines = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    max_x1 = 0
    min_x2 = float('inf') 

    for idx, line in enumerate(lines):
        if idx == i:
            continue
        max_x1 = max(max_x1, line[0])
        min_x2 = min(min_x2, line[1])

    if max_x1 <= min_x2:
        print("Yes")
        exit()

print("No")