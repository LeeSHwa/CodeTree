N = int(input())

icebergs = [int(input()) for _ in range(N)]

max_height = max(icebergs)

max_cnt = 0

for hei in range(1, max_height + 1):
    curr_iceberg = [x - hei for x in icebergs.copy()]
    # print(*curr_iceberg)
    
    flag = True
    cnt = 0
    if curr_iceberg[0] > 0:
        cnt += 1
    else:
        flag = False
        
    for curr_hei in curr_iceberg[1:]:
        if curr_hei > 0:
            if flag == False:
                flag = True
                cnt += 1
        else:
            flag = False
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)