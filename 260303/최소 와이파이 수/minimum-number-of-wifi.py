n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
curr = 0
while curr < n:

    if arr[curr] == 1:
        curr += 2 * m + 1
        cnt += 1
    
    else:
        curr += 1
print(cnt)