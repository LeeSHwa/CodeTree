def solution(n):
    answer = 0
    array = [0] * (n + 1)
    array[0] = 0
    
    def is_not_3x(num):
        
        if num % 3 == 0:
            return False
        
        tmp = str(num)
        if '3' in tmp:
            return False
        
        return True
        
    
    for i in range(1, n + 1):
        pre_num = array[i - 1]
        
        while True:
            if is_not_3x(pre_num + 1):
                array[i] = pre_num + 1
                break
            else:
                pre_num += 1
                
    answer = array[n]
    return answer