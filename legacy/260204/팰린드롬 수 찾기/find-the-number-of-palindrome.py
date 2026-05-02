x, y = map(int, input().split())

cnt = 0
for num in range(x, y + 1):
    str_num = list(map(int, str(num)))
    num_len = len(str_num)
    
    flag = False
    for i in range(num_len // 2):
        if str_num[i] != str_num[-(i + 1)]:
            flag = True
            break

    if flag:
        continue        

    cnt += 1

print(cnt)