N, B = map(int, input().split())

prices = [int(input()) for _ in range(N)]

prices.sort()

price = 0
cnt = 0

for i in range(N):
    if price <= B:
        price += prices[i]
        cnt += 1
        continue
    
    temp = price + prices[i] // 2

    if temp <= B:
        price = temp
        cnt += 1
    
    break

print(cnt)