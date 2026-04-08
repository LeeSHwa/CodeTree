N = int(input())
array = [tuple(map(int, input().split())) for _ in range(N)]
answer = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            
            if i == j or j == k or k == i:
                continue
            
            flag = True
            # i,j,k는 지금 내가 검증할 수
            for num, strike, ball in array:
                cnt_1 = 0
                cnt_2 = 0

                first, second, third = list(map(int, str(num)))
                #f,s,t는 B가 질문한 수
                if i == first : cnt_1 += 1
                if j == second: cnt_1 += 1
                if k == third : cnt_1 += 1

                if first == j or first == k: cnt_2 += 1
                if second == i or second == k : cnt_2 += 1
                if third == i or third == j: cnt_2 += 1

                if cnt_1 != strike or cnt_2 != ball:
                    flag = False
                    break
            
            if flag:
                answer += 1


print(answer)