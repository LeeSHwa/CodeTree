N, B = map(int, input().split())

cost = [tuple(map(int, input().split())) for _ in range(N)]

# cost.sort(key = lambda x : (x[0] + x[1], -x[0]))

discount_cost = [(a // 2, b) for a, b in cost]


ans = 0

for i in range(N):

    curr_cost = cost.copy()
    curr_cost[i] = discount_cost[i]

    curr_cost.sort(key = lambda x : (x[0] + x[1], -x[0]))

    temp = 0
    cnt = 0
    
    for j in range(N):

        temp += sum(curr_cost[j])
                
        if temp > B:
            break
            
        # print(temp, added)

        cnt += 1         

    ans = max(ans, cnt)  

print(ans)
            
    
    