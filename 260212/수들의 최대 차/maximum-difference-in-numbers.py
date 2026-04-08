N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()
# Please write your code here.

max_cnt = 0
for i in range(N):

    curr_min = float('inf')
    curr_max = 0
    temp = [arr[i]]

    for j in range(i + 1, N):

        temp.append(arr[j])
        
        curr_min = min(curr_min, min(temp))
        curr_max = max(curr_max, max(temp))
        
        if curr_max - curr_min > K:
            temp.pop()
            break
    
    max_cnt = max(max_cnt, len(temp))

print(max_cnt)