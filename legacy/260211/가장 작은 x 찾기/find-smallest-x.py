N = int(input())

A_list = []
B_list = []

for _ in range(N):
    a, b = map(int, input().split())
    A_list.append(a)
    B_list.append(b)

for candidate in range(A_list[0] // 2, B_list[0] + 1):
    
    curr_num = candidate * 2
    flag = True
    
    for A, B in zip(A_list, B_list):
        if A <= curr_num and curr_num <= B:
            curr_num *= 2
            continue
        
        flag = False
        break
    
    if flag:
        print(candidate)
        break
    