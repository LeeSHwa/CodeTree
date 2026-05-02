def find_GCD(n, m):
    min_value = min(n, m)
    
    gcd = 1

    for i in range(1, min_value + 1):
        if n % i == 0 and m % i == 0:
            gcd = i
    
    return gcd

n, m = map(int, input().split())

gcd = find_GCD(n, m)

print(gcd)