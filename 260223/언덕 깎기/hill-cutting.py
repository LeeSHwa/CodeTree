n = int(input())

hills = [int(input()) for _ in range(n)]
hills.sort()

max_hei = hills[-1]

min_cost = float('inf')

diff = 17

for hei in range(max_hei - diff + 1):
    left = hei
    right = hei + diff
    
    curr_cost = 0
    
    for hill in hills:
        if hill < left:
            curr_cost += (hill - left) ** 2
        elif hill > right:
            curr_cost += (hill - right) ** 2

    min_cost = min(min_cost, curr_cost)

print(min_cost)    