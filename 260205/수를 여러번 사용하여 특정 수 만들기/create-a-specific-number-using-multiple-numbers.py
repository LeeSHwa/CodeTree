A, B, C = map(int, input().split())

maximum_A = C // A
maximum_B = C // B

if C % A == 0 or C % B == 0:
    print(C)
    exit()

max_sum = 0
for i in range(maximum_A, -1, -1):
    
    for j in range(0, maximum_B + 1):
        
        curr_sum = A * i + B * j

        if curr_sum > C:
            break

        elif curr_sum == C:
            print(C)
            exit()

        else:
            max_sum = max(max_sum, curr_sum)

print(max_sum)