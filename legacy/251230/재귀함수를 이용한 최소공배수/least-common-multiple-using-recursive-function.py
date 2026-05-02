n = int(input())
arr = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a,b)

def cal(n):
    if n == 0:
        return arr[0]
    
    prev_lcm = cal(n - 1)
    return lcm(prev_lcm, arr[n])


print(cal(n-1))