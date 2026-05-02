n, m, c = map(int, input().split())
weight = [list(map(int, input().split())) for _ in range(n)]

max_price = 0

# array에서 m개 요소 이하로 c보다 작게 만들 수 있는지 확인하고, 최대 값을 반환하는 함수
def recurr(array, idx, curr_sum, curr_price):
    global max_price
    
    # 종료조건
    if idx == m:
        max_price = max(max_price, curr_price)
        return
    
    # 1. 포함하고 탐색
    if curr_sum + array[idx] <= c:
        recurr(array, idx + 1, curr_sum + array[idx], curr_price + array[idx] ** 2)

    # 2. 포함하지 않고 탐색
    recurr(array, idx + 1, curr_sum, curr_price)
    
mapping_table = [[0] * (n - m + 1) for _ in range(n)]

# mapping table
array = []
for i in range(n):
    for j in range(n - m + 1):
        max_price = 0
        array = weight[i][j : j + m]
        recurr(array, 0, 0, 0)
        mapping_table[i][j] = max_price

ans = 0
# 2차원 배열에서 합이 가장 큰 조합 찾기 문제로 치환
for f_row in range(n):
    for f_col in range(n - m + 1):
        
        for s_row in range(n):
            
            if f_row == s_row and f_col + m < n - m + 1:
                for s_col in range(f_col + m, n - m + 1):
                    ans = max(ans, mapping_table[f_row][f_col] + mapping_table[s_row][s_col])
            
            
            if s_row != f_row:
                for s_col in range(n - m + 1):
                    ans = max(ans, mapping_table[f_row][f_col] + mapping_table[s_row][s_col])

print(ans)              
                