n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = max(arr)
for candidate in range(ans, 0, -1):
    
    jump = 1
    # print(f"candidate is {candidate}")
    flag = True
    for i in range(n):
        if jump > k:
            flag = False
            break 
        
        if arr[i] <= candidate:
            jump = 1
            continue
            # print(f"{arr[i]} jump!")
        else:
            jump += 1
            # print(f"{arr[i]} can't jump...")

            
    if flag:
        ans = min(ans, candidate)

print(ans)