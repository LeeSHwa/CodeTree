def find_gcd(n, m):
    while m:
        n, m = m, n%m
    
    return n


def find_lcm(n, m, gcd):
    term = gcd
    while True:
        if gcd % n == 0 and gcd % m == 0:
            lcm = gcd
            return lcm
            break
        else: 
            gcd += term


n, m = map(int, input().split())

gcd = find_gcd(n, m)
print(find_lcm(n, m, gcd))