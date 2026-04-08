K, N = map(int, input().split())
ranks = [list(map(int, input().split())) for _ in range(K)]

ans = []

for i in range(1, N + 1):

    std = i
    for j in range(1, N + 1):
        if j == i:
            continue
        flag = True
        
        for rank in ranks:
            one = rank.index(i)
            two = rank.index(j)

            if two > one:
                flag = False
        
        if flag:
            ans.append((i, j))

print(len(ans))