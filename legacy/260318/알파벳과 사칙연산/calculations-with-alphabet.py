expression = list(input())
N = len(expression)
# Please write your code here.

mapping_table = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5}
alphas = [0, 0, 0, 0, 0, 0]
is_exist = [False] * 6

for alpha in mapping_table.keys():
    if alpha in expression:
        is_exist[mapping_table[alpha]] = True


def cal_exp():
    if N == 1:
        return 4

    idx = 1
    num = alphas[ord(expression[0]) - ord('a')]
    oper = None
    
    while idx < N:
        oper = expression[idx]
        next_num = alphas[ord(expression[idx + 1]) - ord('a')]

        if oper == '+': num += next_num
        elif oper == '-': num -= next_num
        elif oper == '*': num *= next_num
        
        idx += 2

    return num

max_result = -float('inf')

def recurr(idx):
    global max_result

    if idx == 6:

        curr_result = cal_exp()

        if curr_result > max_result:
            max_result = curr_result
        
        return
    
    if is_exist[idx]:
        for num in range(4, 0, -1):
            alphas[idx] = num

            recurr(idx + 1)
    else:
        recurr(idx + 1)

recurr(0)

print(max_result)