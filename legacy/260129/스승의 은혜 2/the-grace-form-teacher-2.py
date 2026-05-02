N, B = map(int, input().split())

prices = [int(input()) for _ in range(N)]

prices.sort()

price = 0
cnt = 0

for i in range(N):
    temp = price + prices[i]

    if temp <= B:
        cnt += 1
        price = temp
        continue
    
    temp = price + prices[i] // 2

    if temp <= B:
        price = temp
        cnt += 1
    
    break

print(cnt)