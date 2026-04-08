N = int(input())

dots = [tuple(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')

for i in range(N - 1):
    curr_x = dots[i][0]
    curr_y = dots[i][1]

    for j in range(i + 1, N):
        next_x = dots[j][0]
        next_y = dots[j][1]

        min_diff = min(min_diff, (curr_x - next_x)**2 + (curr_y - next_y)**2)

print(min_diff)