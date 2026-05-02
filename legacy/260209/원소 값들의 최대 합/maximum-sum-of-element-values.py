n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.

max_sum = 0
for i in range(1, n + 1):
    curr_sum = 0
    pos = i

    for _ in range(m):
        curr_sum += arr[pos]
        pos = arr[pos]
    
    max_sum = max(max_sum, curr_sum)

print(max_sum)
    