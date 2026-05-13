def solution(n):
    MOD = 1000000007
    
    if n % 2 == 1:
        return 0
    
    dp = [0] * (n + 4)
    
    dp[2] = 3    
    dp[4] = 11
    
    for i in range(6, n + 1, 2): # 6부터 n까지, 짝수만 가능
        dp[i] = (dp[i] + dp[i-2] * 3) % MOD
        
        for j in range(i - 4, 1, -2): # dp[i-4]부터 dp[2]까지 계속 2의 배수만큼 곱해서 합해야함
            dp[i] = (dp[i] + dp[j] * 2) % MOD
            
        dp[i] += 2
    
    answer = dp[n]
    
    return answer