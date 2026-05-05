n = int(input())
nums = list(map(int, input().split()))
S = sum(nums)
target = S // 2

# A의 값을 X라고 했을 때, B의 값은 자동적으로 S - X
# 그렇다면 둘의 차이값은 |S - 2X|

# A 배열만 관리한다면, 차이값만 최소로 갱신해 나가면 정답?

# A 배열 (만들 수 있는지?)
dp = [False] * (target + 1)

dp[0] = True

for num in nums:

    for x in range(target, num - 1, -1):
        if dp[x - num]:
            dp[x] = True

for i in range(target, -1, -1):
    if dp[i]:
        print(S - 2 * i)
        break