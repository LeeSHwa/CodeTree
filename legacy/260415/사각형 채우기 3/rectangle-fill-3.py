n = int(input())

# Please write your code here.
UNUSED = -1
MAX_N = 1001
MOD = 1000000007

memo = [UNUSED for _ in range(MAX_N)]
memo[0] = 1
memo[1] = 2
memo[2] = 7

for i in range(3, n + 1):
    memo[i] = (memo[i-1] * 2 + memo[i-2] * 3) % MOD
    
    for j in range(i - 3, -1, -1):
        memo[i] = (memo[i] + memo[j] * 2) % MOD

print(memo[n])