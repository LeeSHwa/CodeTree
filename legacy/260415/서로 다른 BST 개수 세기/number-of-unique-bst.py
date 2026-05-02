n = int(input())

# Please write your code here.

UNUSED = 0
MAX_N = 20
memo = [UNUSED for _ in range(MAX_N)]

memo[0] = 1
memo[1] = 1

for i in range(2, n + 1):
    
    for j in range(i):
        memo[i] += memo[j] * memo[i - j -1]

print(memo[n])
    
    