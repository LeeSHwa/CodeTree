from collections import defaultdict

n, k = map(int, input().split())
booms = defaultdict(list)

def is_explosion(array):
    length = len(array)
    explosion = set()
    last_num = array[0]

    for idx in range(1, length):
        if array[idx] - last_num <= k:
            explosion.add(array[idx])
            explosion.add(last_num)

        last_num = array[idx]
    
    return len(explosion)

for idx in range(n):
    boom = int(input())

    booms[boom].append(idx)
    
for elem in booms:
    booms[elem] = is_explosion(booms[elem])
    if booms[elem] > 0:
        flag = False

ans = sorted(booms.items(), key = lambda x : (-x[1], -x[0]))

if ans[0][1] < 1:
    print(0)
else:
    print(ans[0][0])