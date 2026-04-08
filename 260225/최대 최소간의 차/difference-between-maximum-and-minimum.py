n, k = map(int, input().split())

nums = list(map(int, input().split()))

min_num = min(nums)
max_num = max(nums)

ans = float('inf')

for start in range(min_num, max_num):
    end = start + k
    total_diff = 0
    
    for num in nums:
        if start <= num <= end:
            continue
        else:
            diff = min(abs(start - num), abs(end - num))
            total_diff += diff        

    ans = min(ans, total_diff)

print(ans)