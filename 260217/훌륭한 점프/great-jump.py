n, k = map(int, input().split())
arr = list(map(int, input().split()))

candidates = sorted(arr, reverse = True)
ans = float('inf')

for candidate in candidates:
    
    jump = 1
    # print(f"candidate is {candidate}")
    flag = True

    if arr[0] > candidate or arr[-1] > candidate:
        continue
    
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