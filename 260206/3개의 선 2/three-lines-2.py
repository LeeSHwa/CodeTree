from collections import defaultdict

nums = defaultdict(list)

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    nums[x].append(y)

    if len(nums) > 3 and len(nums[x]) > 3:
        print(0)
        exit()


print(1)