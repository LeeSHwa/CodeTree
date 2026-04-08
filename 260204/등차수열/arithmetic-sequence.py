N = int(input())

nums = list(map(int, input().split()))

nums.sort()

max_cnt = 0
for K in range(1, 101):
    cnt = 0
    for num in nums:
        if K > num:
            diff = K - num

            if K + diff in nums:
                cnt += 1   

    max_cnt = max(max_cnt, cnt)
print(max_cnt)