N = int(input())

nums = list(map(int, input().split()))

for i in range(1, N):
    curr_nums = [i]
    flag = False

    for j in range(N - 1):
        curr_num = nums[j] - curr_nums[j]
        if curr_num <= 0:
            flag = True
            break
        curr_nums.append(curr_num)
    if flag:
        continue
    
    if len(set(curr_nums)) == N:
        print(*curr_nums)
        exit()