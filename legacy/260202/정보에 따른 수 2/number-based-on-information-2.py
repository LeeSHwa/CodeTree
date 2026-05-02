T, a, b = map(int, input().split())

MAX_RANGE = 1000
array = [0] * (MAX_RANGE + 1)

min_x = MAX_RANGE
max_x = 0

for _ in range(T):
    alpha, x = input().split()
    x = int(x)
    
    array[x] = alpha
    min_x = min(min_x, x)
    max_x = max(max_x, x)

# 어떻게 미리 다 조사해놓을 수 있을까

S_list = [MAX_RANGE] * (max_x + 2)
N_list = [MAX_RANGE] * (max_x + 2)

for idx in range(min_x, max_x + 1):
    temp = array[idx]
    
    S_list[idx] = 0 if temp == "S" else S_list[idx - 1] + 1
    N_list[idx] = 0 if temp == "N" else N_list[idx - 1] + 1

for idx in range(max_x, min_x - 1, -1):
    temp = array[idx]

    S_temp = 0 if temp == "S" else S_list[idx + 1] + 1
    N_temp = 0 if temp == "N" else N_list[idx + 1] + 1
    
    S_list[idx] = min(S_list[idx], S_temp)
    N_list[idx] = min(N_list[idx], N_temp)
    
cnt = 0
for idx in range(a, b+1):
    d1 = S_list[idx]
    d2 = N_list[idx]

    if d1 <= d2:
        cnt += 1

print(cnt)