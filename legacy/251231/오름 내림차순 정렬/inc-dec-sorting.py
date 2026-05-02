n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.


asc = sorted(nums)
desc = sorted(nums, reverse=True)

print(' '.join(map(str, asc)))
print(' '.join(map(str, desc)))
