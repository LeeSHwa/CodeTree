# 10:47

n, m = map(int, input().split())

# nums = list(map(bin,(map(int, input().split()))))
# nums = [list(map(int, (x[2:]))) for x in nums]

nums = list(map(int, input().split()))

# def bin_to_dec(array):
#     length = len(array)
#     decimal = 0
#     for i in range(length):
#         decimal += array[-(i + 1)] * 2 ** i

#     return decimal

# def xor(num1, num2):
#     num1_len = len(num1)
#     num2_len = len(num2)

#     max_len = max(num1_len, num2_len)
    
#     bigger = []
#     small = []

#     if num1_len == max_len:
#         bigger = num1
#         small = num2
#     else:
#         small = num1
#         bigger = num2
#     small = small[: : -1]

#     while len(small) < max_len:
#         small.append(0)
#     small = small[: : -1]

#     result = []

#     for i in range(max_len):
#         if small[i] + bigger[i] == 1:
#             result.append(1)
#         else:
#             result.append(0)
    
#     return result
    
ans = 0

def backtrack(idx, cnt, current_num):
    global ans 
    
    if cnt == m:
        # ans = max(ans, bin_to_dec(current_num))
        ans = max(ans, current_num)
        return
    
    if idx == n:
        return
    
    if cnt == 0:
        backtrack(idx + 1, 1, nums[idx])
    else:
        # backtrack(idx + 1, cnt + 1, xor(current_num, nums[idx]))
        backtrack(idx + 1, cnt + 1, current_num ^ nums[idx])

    # backtrack(idx + 1, cnt, current_num)
    backtrack(idx + 1, cnt, current_num)


# backtrack(0, 0, [])
backtrack(0, 0, 0)

print(ans)
        