n = int(input())

# Please write your code here.

def cal(N):
    if N == 1:
        return 0

    if N % 2 == 0:
        N //= 2
        return cal(N) + 1        
    
    else:
        N = N * 3 + 1
        return cal(N) + 1        
    

print(cal(n))