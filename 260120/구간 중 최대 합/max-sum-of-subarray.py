N, K = map(int, input().split())

nums = list(map(int, input().split()))
sum_of_nums = []

for idx in range(N - K + 1): # 5개의 수 중 3개의 연속된 수라면? 0, 1, 2까지 탐색
    sum_of_nums.append(sum(nums[idx : idx + K]))

print(max(sum_of_nums))