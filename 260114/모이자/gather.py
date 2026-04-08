N = int(input())

houses = list(map(int, input().split()))

min_value = float('inf')

for i in range(N):
    std = houses[i]

    temp = 0

    for j in range(N):
        temp += abs(j - i) * houses[j]
    
    min_value = min(min_value, temp)

print(min_value)