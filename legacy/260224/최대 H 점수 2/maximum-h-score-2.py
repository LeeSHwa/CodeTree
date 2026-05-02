from itertools import zip_longest

N, L = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

L_list = [1] * L

def is_possible(H, arr):
    cnt = 0
    for num in arr:
        if num >= H:
            cnt += 1
    
    return cnt >= H

ans = 0
for h in range(101):
    
    temp = [x for x in nums if x >= h]

    temp2 = [x + y for x, y in zip_longest(temp, L_list, fillvalue = 0)]

    if is_possible(h, temp2):
        ans = max(h, min(temp2))

print(ans)