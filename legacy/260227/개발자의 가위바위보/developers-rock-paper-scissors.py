n = int(input())

nums = []

rsp = ['r', 's', 'p']

for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        continue

    nums.append(tuple([a, b]))

def who_win(a, b):
    if a == 'r' and b == 's':
        return 1
    
    elif a == 's' and b == 'p':
        return 1
    
    elif a == 'p' and b == 'r':
        return 1
    
    else: 
        return 0

ans = 0
for i in range(3):
    for j in range(3): # i = 1, j = 2
        if j == i:
            continue
        table = {1 : rsp[i], 2 : rsp[j], 3 : rsp[3 - i - j]}
        curr_win = 0
        for a, b in nums: # 1, 3

            curr_win += who_win(table[a], table[b])
            # print(a, b, curr_win)

        ans = max(ans, curr_win)

print(ans)  