n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

diff = [a - b for a, b in zip(A, B)]

ans = 0
curr_diff = 0
for i in range(n):
    curr_diff += diff[i]
    ans += curr_diff

print(ans)