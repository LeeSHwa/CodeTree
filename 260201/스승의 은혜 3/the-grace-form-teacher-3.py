N, B = map(int, input().split())

cost = [tuple(map(int, input().split())) for _ in range(N)]

cost.sort(key = lambda x : (x[0] + x[1], -x[0]))

discount_cost = [(a // 2, b) for a, b in cost]


# 누적합?? 어떻게 쌓아가지??
# 기회가 1번임
# 한계에 달할때?? 근데 이걸 누적합으로 어떻게 하고싶은데...
# 흠.. 
# 그냥 그럼 처음부터 끝까지 한 번씩 다 썼을때 가장 큰 경우를 계속 갱신

ans = 0

for i in range(N):

    temp = 0
    cnt = 0
    
    for j in range(N):
        if j == i:
            curr_discount_sum = sum(discount_cost[j])
            temp += curr_discount_sum
        else:
            curr_sum = sum(cost[j])
            temp += curr_sum

        if temp > B:
            break

        cnt += 1         

    ans = max(ans, cnt)  

print(ans)
            
    
    