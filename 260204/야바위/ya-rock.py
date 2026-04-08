one = 0
two = 0
three = 0

N = int(input())

cups = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0
for ball in range(1, 4):
    cup = [0] * 4
    cup[ball] = 1    

    cnt = 0
    for a, b, c in cups:
        cup[a], cup[b] = cup[b], cup[a]
        cnt += cup[c]

    max_cnt = max(max_cnt, cnt)

print(max_cnt)