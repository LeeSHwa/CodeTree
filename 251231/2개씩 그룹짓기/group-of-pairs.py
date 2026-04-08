n = int(input())
nums = sorted(list(map(int, input().split()))) # 2 3 5 5

# Please write your code here.

max_num = -1
for i in range(n):             # 2 ( 0 ~ 1 )
    temp = nums[i] + nums[-(1+i)] # nums[0] + nums[-1] / nums[1] + nums[-2]
    max_num = max(max_num, temp)  # max(-1, 7) -> 7 / max(7, 8) -> 8

print(max_num) # 8