import sys
input = sys.stdin.readline

m = int(input())
a, b = map(int, input().split())

def cal(target):
    left = 1
    right = m

    cnt = 1
    
    while left <= right:
        mid = (left + right) // 2

        if mid == target:
            return cnt
        
        if mid >= target:
            right = mid - 1
        else:
            left = mid + 1
        cnt += 1

min_cnt = m
max_cnt = -1

for num in range(a, b + 1):
    cnt = cal(num)
    min_cnt = min(min_cnt, cnt)
    max_cnt = max(max_cnt, cnt)

print(min_cnt, max_cnt)