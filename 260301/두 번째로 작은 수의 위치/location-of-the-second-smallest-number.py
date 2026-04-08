import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))

min_num = min(nums)
set_nums = set(nums)

if len(set_nums) == 1:
    print(-1)
    exit()

set_nums.remove(min_num)

second_min_num = min(set_nums)

if nums.count(second_min_num) > 1:
    print(-1)
    exit()

for i in range(n):
    if nums[i] == second_min_num:
        print(i + 1)
        break