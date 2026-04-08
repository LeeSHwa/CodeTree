N = int(input())

nums = list(map(int, input().split()))

count = 0

for i in range(N): # 2
    for j in range(i+1, N+1): # 5

        window = nums[i:j] # 2, 3, 4
        
        current_sum = sum(window)
        length = j - i

        if (current_sum % length) == 0:
            avg = current_sum // length

            if avg in window:
                count += 1
        
        # print((sum(window) // (j-i)) , window)

print(count)