n = int(input())

nums = list(map(int, input().split()))

total_sum = sum(nums)

ans = float('inf')

def backtrack(idx, selected_nums, current_sum):
    global ans
    
    if selected_nums == n:
        ans = min(ans, abs(2 * current_sum - total_sum))
        return
         
    if idx == 2 * n:
        return
    
    backtrack(idx + 1, selected_nums + 1, current_sum + nums[idx])
    backtrack(idx + 1, selected_nums, current_sum)

backtrack(0, 0, 0)
print(ans)