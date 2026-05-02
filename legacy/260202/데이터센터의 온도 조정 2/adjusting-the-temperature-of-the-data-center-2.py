N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.

min_ta = 1001
max_tb = 0

for a, b in ranges:
    min_ta = min(min_ta, a)
    max_tb = max(max_tb, b)

max_work = 0

for temper in range(min_ta - 1, max_tb + 2):

    work = 0

    for ta, tb in ranges:
        if temper < ta:
            work += C

        elif ta <= temper and temper <= tb:
            work += G

        else:
            work += H

    max_work = max(max_work, work)

print(max_work)                
