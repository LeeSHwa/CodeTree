n = int(input())

nums = list(map(int, input().split()))

memo = [0] * n
memo[0] = 1

def dp(idx):
    
    num = nums[idx]

    max_len = 0

    for i in range(idx):
        if nums[i] < num:
            max_len = max(max_len, memo[i])
    
    memo[idx] = max_len + 1

for i in range(1, n):
    dp(i)
    
print(max(memo))