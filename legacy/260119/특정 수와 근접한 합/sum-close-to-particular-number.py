N, S = map(int, input().split())

nums = list(map(int, input().split()))


all_sum = sum(nums)
mins = float('inf')

for i in range(N-1):
    for j in range(i+1, N):
        temp = all_sum
        
        aaa = abs(temp - nums[i] - nums[j]) # 전체 합에서 두 수를 뺌

        mins = min(mins, abs(S - aaa))           

print(mins)                        # mins와 S의 차이
            