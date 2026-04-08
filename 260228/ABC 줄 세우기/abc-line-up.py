n = int(input())

alphas = list(input().split())

cnt = 0
while True:
    flag = True

    for i in range(n-1):
        if alphas[i] > alphas[i+1]:
            flag = False
            alphas[i], alphas[i+1] = alphas[i+1], alphas[i]
            cnt += 1
    
    if flag:
        break

print(cnt)