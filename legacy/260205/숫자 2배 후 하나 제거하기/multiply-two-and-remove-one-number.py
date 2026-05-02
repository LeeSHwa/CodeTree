N = int(input())

nums = list(map(int, input().split()))

min_diff = float('inf')

for i in range(N):
    nums[i] *= 2 # 하나의 숫자를 선택해 2배를 한 후

    for j in range(N):
        temp_arr = []
        
        curr_sum = 0
        for k in range(N): 
            if k == j:
                continue
            else:
                temp_arr.append(nums[k]) # 다시 하나의 숫자를 선택해 제거
            
            length = len(temp_arr)
            
            if length >= 2:
                curr_sum += abs(temp_arr[length - 1] - temp_arr[length - 2])
        
        min_diff = min(min_diff, curr_sum)

    nums[i] //= 2


print(min_diff)