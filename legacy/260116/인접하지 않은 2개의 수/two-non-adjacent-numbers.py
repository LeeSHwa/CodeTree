N = int(input())
nums = list(map(int, input().split()))

big = -1 
for idx in range(N):
    
    for num in nums[idx + 2 :]:
        big = max(big, nums[idx] + num) 


print(big)   
