n = int(input())

# Please write your code here.

MAX_N = 1001
UNUSED = -1
MOD = 10007

memo = [UNUSED for _ in range(MAX_N)]

memo[0] = 1
memo[1] = 1
memo[2] = 3

for i in range(3, n + 1):
    memo[i] = (memo[i-1] + 2 * memo[i-2]) % MOD

print(memo[n])