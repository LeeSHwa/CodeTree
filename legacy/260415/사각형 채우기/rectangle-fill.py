n = int(input())

UNUSED = -1

memo = [UNUSED for _ in range(n + 1)]

memo[1] = 1
memo[2] = 2

for idx in range(3, n + 1):
    memo[idx] = (memo[idx-1] + memo[idx-2]) % 10007

print(memo[n])