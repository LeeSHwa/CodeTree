N, M = map(int, input().split())

nums = list(map(int, input().split()))

def is_possible(max_sum, n, m, nums):
    curr_sum = 0
    section = 1

    for num in nums:
        if curr_sum + num > max_sum:
            section += 1
            curr_sum = num
        else:
            curr_sum += num    
    
    return section <= m

# 최대값의 범위
left = max(nums)
right = sum(nums)

# 만약 is_possible하다? 최대값을 더 줄여보고
# 안된다면 최소값을 더 높여보는걸로?

ans = 0
while left <= right:
    mid = (left + right) // 2
    
    if is_possible(mid, N, M, nums):
        right = mid - 1
        ans = mid
    else:
        left = mid + 1

print(ans)