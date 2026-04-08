N = input() # 입력 문자열
M = input() # 목적 문자열

def is_substring(M):
    len_M = len(M)
    count = 0

    for i in range(len(N) - len_M + 1):
        window = N[i:i+len_M]
        if window == M:
            return count
        else:
            count += 1
    
    return -1

result = is_substring(M)
print(result)

    